#!/usr/bin/env python
import os

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")


@app.route('/api/search')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    # db = client.faces
    # face = {
    #     "name": "Mike",
    #     "text": "My first face!",
    # }
    # face_id = db.faces.insert_one(face).inserted_id
    # return f'{face_id}'
    return { 'message': 'Hello' }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get(
        "FLASK_SERVER_PORT", 9090), debug=True)
