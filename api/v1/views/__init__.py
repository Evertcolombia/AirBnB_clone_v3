#!/usr/bin/python3
""" init the blueprint module for views components"""

from flask import Blueprint


app_views = Blueprint('status', __name__,
                        url_prefix='/api/v1')

from api.v1.views.index import *
