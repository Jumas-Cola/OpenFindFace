#!/usr/bin/env python
import os
import uuid
from db import dbClient
from face_repository import FaceRepository

from flask import Flask
from flask import request
from flask import json
from werkzeug.utils import secure_filename
import face_recognition

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

face_repo = FaceRepository()


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/search', methods=['POST'])
def search():
    file = request.files['image']
    if file and allowed_file(file.filename):
        file_uuid = str(uuid.uuid4())
        filename = secure_filename(f'{file_uuid}_{file.filename}')
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)
        known_image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(known_image)
        os.remove(image_path)

        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]
            faces = face_repo.get_by_array(face_encoding)

            data = []
            for face in faces:
                data_item = json.loads(face['data'])
                data_item['id'] = str(face.get('_id'))
                data.append(data_item)

            if data:
                response = app.response_class(
                    response=json.dumps(data, ensure_ascii=False),
                    status=200,
                    mimetype='application/json'
                )
                return response

            response = app.response_class(
                response={'message': 'error'},
                status=404,
                mimetype='application/json'
            )
            return response

    response = app.response_class(
        response=json.dumps({
            'message': 'error',
        }),
        status=422,
        mimetype='application/json'
    )
    return response


@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)
        known_image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(known_image)

        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]
            faces = list(face_repo.get_by_array(face_encoding))
            if not faces:
                data = json.loads(request.form.get('data'))
                data["image"] = image_path
                face_repo.create(data, face_encoding)

            response = app.response_class(
                response=json.dumps({
                    'message': 'success',
                }),
                status=200,
                mimetype='application/json'
            )
            return response

        os.remove(image_path)

    response = app.response_class(
        response=json.dumps({
            'message': 'error',
        }),
        status=422,
        mimetype='application/json'
    )
    return response


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=os.environ.get(
#         "FLASK_SERVER_PORT", 9090), debug=True)
