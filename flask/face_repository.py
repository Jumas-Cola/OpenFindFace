from db import dbClient
import json
from numpy import ndarray
import numpy as np


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


class FaceRepository:
    def __init__(self):
        self.db = dbClient

    def get_by_array(self, face_encoding: ndarray):
        # TODO: Переписать на более оптимальное сравнение
        faces = self.db.faces.faces.find({})
        for face in faces:
            results = compare_faces([face_encoding], np.array(face['image']))
            if results[0]:
                return face
        return False

    def create(self, data: dict, face_vector: ndarray):
        face_data = {
            "data": json.dumps(data, ensure_ascii=False),
            "image": list(face_vector)
        }
        
        self.db.faces.faces.insert_one(face_data)

