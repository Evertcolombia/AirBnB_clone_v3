#!/usr/bin/python3
""" Views to index resoyrce for components"""
from flask import jsonify
from api.v1.views import app_views
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ get the status resources """
    obj = {"status": "OK"}
    return jsonify(obj), 200


@app_views.route("/stats", strict_slashes=False, methods=['GET'])
def stats():
    """ the all stats """
    all_cls = {
        'amenities': 0, 'cities': 0, 'places': 0,
        'reviews': 0, 'states': 0, 'users': 0}

    for key, values in all_cls.items():
        values = storage.count(key)
    return jsonify(all_cls), 200
