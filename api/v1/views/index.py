#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    obj = {"status": "OK"}
    return jsonify(obj), 200
