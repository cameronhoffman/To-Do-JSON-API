from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

from controllers import itemlist_controller, item_controller
from models import ItemList, Item

app = Flask(__name__)

def model_array_to_list(array):
    """Converts the enumeration of PeeWee models to a list of dictionaries.

    :param array: A list of dictionaries representing the models
    """
    return list(map(lambda l: model_to_dict(l), array))

@app.route('/')
def healthcheck():
    """A simple healthcheck route"""
    return 'ok'

@app.route('/lists')
def get_all_itemlists():
    """Gets all of the itemlists"""
    item_lists = itemlist_controller.get_all_itemlists() # Returns itemlist model array
    return jsonify(model_array_to_list(item_lists))

@app.route('/lists', methods=['POST'])
def create_list():
    """Creates a list based on the request body"""
    try:
        body = request.get_json()
    except:
        return "(List Creation) JSON request parsing failed.", 400 # Catch BadRequest from get_json->on_json_loading_failed
    else:
        if body['name'] == None: 
            return "(List Creation) No value to initialize list name.", 422
        else:
            itemlist = itemlist_controller.create_itemlist(body) # Returns itemlist model
            return jsonify(model_to_dict(itemlist)), 201

@app.route('/lists/<listitem_id>')
def get_itemlist(listitem_id):
    """Gets itemlist with given ID"""
    itemlist = itemlist_controller.get_itemlist(listitem_id) # Returns itemlist model
    return jsonify(model_to_dict(itemlist)), 200

@app.route('/lists/<listitem_id>', methods=['PUT'])
def update_itemlist(listitem_id): 
    """Update itemlist based on the request body"""
    try:
        body = request.get_json()
    except:
        return "(List Update) JSON request parsing failed.", 400 # Catch BadRequest from get_json->on_json_loading_failed
    else:
        if body['name'] == None: # for test_update_item_failure test. You should be able to update and not send a new name?
            return "(List Update) No value to update list name.", 422
        else:
            itemlist = itemlist_controller.update_itemlist(listitem_id, body) # Returns itemlist model
            return jsonify(model_to_dict(itemlist)), 200

@app.route('/lists/<listitem_id>', methods=['DELETE'])
def delete_itemlist(listitem_id):
    """Delete itemlist with the given ID"""
    itemlist_controller.delete_itemlist(listitem_id)
    return "(List Delete) List deleted.", 404

@app.route('/lists/<listitem_id>/items')
def get_items_by_list(listitem_id):
    """Return items with the given ID"""
    items = item_controller.get_items_by_list(listitem_id) # Returns item model array
    return jsonify(model_array_to_list(items)), 200

@app.route('/items', methods=['POST'])
def create_item():
    """Creates item based on the request body"""
    try:
        body = request.get_json()
    except:
        return "(Create Item) JSON Request Parsing Failed.", 400 # Catch BadRequest from get_json->on_json_loading_failed
    else:
        if body['name'] == None:
            return "(Create Item) No value to initialize item name.", 422
        else:
            item = item_controller.create_item(body) # Returns item model
            return jsonify(model_to_dict(item)), 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    """Updates item based on the request body"""
    try:
        body = request.get_json()
    except:
        return "(Item Update) JSON request parsing failed.", 400 # Catch BadRequest from get_json->on_json_loading_failed
    else:
        if body['name'] == None:
            return "(Item Update) No value to update item name.", 422
        else:
            item = item_controller.update_item(item_id, body) # Returns item model
            return jsonify(model_to_dict(item)), 200

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Deletes a single item with the given ID"""
    item_controller.delete_item(item_id)
    return "(Item Delete) Item deleted.", 404
