#!/usr/bin/env python
import os
from numpy import ndarray
import numpy as np
import uuid

from flask import Flask, render_template
from flask import request
from flask import json
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import face_recognition

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

client = MongoClient("mongo:27017")


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def face_distance(face_encodings: list, face_to_compare: ndarray) -> ndarray:
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the faces are.

    :param face_encodings: List of face encodings to compare
    :param face_to_compare: A face encoding to compare against
    :return: A numpy ndarray with the distance for each face in the same order as the 'faces' array
    """
    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)


def compare_faces(known_face_encodings: list, face_encoding_to_check: ndarray, tolerance: float = 0.6) -> list:
    """
    Compare a list of face encodings against a candidate encoding to see if they match.

    :param known_face_encodings: A list of known face encodings
    :param face_encoding_to_check: A single face encoding to compare against the list
    :param tolerance: How much distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.
    :return: A list of True/False values indicating which known_face_encodings match the face encoding to check
    """
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)


def get_face(db: MongoClient, face_encoding: ndarray):
    # TODO: Переписать на более оптимальное сравнение
    faces = db.faces.find({})
    for face in faces:
        results = compare_faces([face_encoding], np.array(face['image']))
        if results[0]:
            return face
    return False


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

            db = client.faces
            face = get_face(db, face_encoding)

            if face:
                response = app.response_class(
                    response=face['data'],
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

            db = client.faces
            face = get_face(db, face_encoding)
            data = json.loads(request.form.get('data'))
            data["image"] = image_path
            if not face:
                face_data = {
                    "data": json.dumps(data, ensure_ascii=False),
                    "image": list(face_encoding)
                }
                db.faces.insert_one(face_data)

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get(
        "FLASK_SERVER_PORT", 9090), debug=True)
