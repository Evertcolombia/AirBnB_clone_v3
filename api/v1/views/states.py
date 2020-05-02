#!/usr/bin/python3
"""
Blueprint for State objs that handles all default RestFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, Blueprint, Flask
from models import storage
from models.state import State
from flask import make_response


@app_views.route('/states', methods=["GET"], strict_slashes=False)
def state():
    """ Retrieves State obj """
    states = []
    my_states = storage.all('State').values()
    for my_state in my_states:
        states.append(my_state.to_dict())
    return jsonify(states)


@app_views.route('/states/<string:state_id>',
                 methods=['GET'],
                 strict_slashes=False)
def state_id(state_id):
    """Retrieve an object into a valid JSON"""
    my_state = storage.get('State', state_id)
    if my_state is None:
        abort(404)
    return jsonify(my_state.to_dict())


@app_views.route('/states/<s_id>', methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State obj based on its' id """

    my_state = storage.get('State', state_id)
    if my_state is None:
        abort(404)
    my_state.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states', methods=["POST"], strict_slashes=False)
def create_state():
    """
    Creates a State
    """
    if not request.json:
        abort(400, 'Not a JSON')
    if 'name' not in request.json:
        abort(400, 'Missing name')
    my_state = state.State(name=request.json.get('name', ""))
    storage.new(my_state)
    my_state.save()
    return make_response(jsonify(my_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=["PUT"], strict_slashes=False)
def update_states(state_id):
    """
    Updates a State obj & id
    """
    my_state = storage.get('State', state_id)
    if my_state is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    for req in request.json:
        if req not in ['id', 'created_at', 'updated_at']:
            setattr(my_state, req, request.json[req])
    my_state.save()
    return jsonify(my_state.to_dict())
