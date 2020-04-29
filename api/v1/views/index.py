#!/usr/bin/python3
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
    obj = {"status": "OK"}
    return jsonify(obj), 200

@app_views.route("/stats", strict_slashes=False, methods=['GET'])
def stats():
    """ the all stats """
    classes = {
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User)}
    return jsonify(classes), 200
