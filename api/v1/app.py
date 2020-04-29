#!/usr/bin/python3
"""
Handles API status of our Flask instance 'app'
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def deardown_db(exception):
    """ closes storage sesson on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST") or "0.0.0.0",
            port=getenv("HBNB_API_PORT") or 5000, threaded=True)
