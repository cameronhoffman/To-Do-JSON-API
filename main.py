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
    item_lists = itemlist_controller.get_all_itemlists()

    return jsonify(model_array_to_list(item_lists))

@app.route('/lists', methods=['POST'])
def create_list():
    """Creates a list based on the request body"""
    try:
        body = request.get_json()
    except:
        return "(List Creation) JSON request parsing failed.", 400 # Catch BadRequest from get_json
    else:
        if body['name'] == None: 
            return "(List Creation) No value to initialize list name.", 422
        else:
            itemlist = itemlist_controller.create_itemlist(body)
            return jsonify(model_to_dict(itemlist)), 201

@app.route('/lists/<listitem_id>')
def get_itemlist(listitem_id):
    itemlist = ItemList.get(ItemList.id == 'listitem_id')
    return jsonify(model_array_to_list(itemlist))

@app.route('/lists/<listitem_id>', methods=['PUT'])
def update_itemlist(listitem_id):
    try:
        body = request.get_json()
    except:
        return "(List Update) JSON Request Parsing Failed.", 400 # Catch BadRequest from get_json
    else:
        if body['name'] == None:
            return "(List Update) No value to update list name.", 422
        else:
            itemlist = itemlist_controller.update_itemlist(listitem_id, body)
            return get_itemlist(listitem_id), 200

@app.route('/lists/<listitem_id>', methods=['DELETE'])
def delete_itemlist(listitem_id):
    itemlist_controller.delete_itemlist(listitem_id)
    return "(List Delete) List deleted.", 404

@app.route('/lists/<listitem_id>/items')
def get_items_by_list(listitem_id):
    items = item_controller.get_items_by_list(listitem_id)
    return jsonify(model_array_to_list(items)), 200

## Not-Implemented

@app.route('/items', methods=['POST'])
def create_item():
    try:
        body = request.get_json()
    except:
        return "(Create Item) JSON Request Parsing Failed.", 400
    else:
        if body['name'] == None:
            return "(Create Item) No value to initialize item name.", 422
        else:
            item = item.controller.create_item(body)
            return jsonify(model_to_dict(item)), 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    """Updates a single item by ID"""
    raise Exception('Implement this route')

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Deletes a single item by ID"""
    raise Exception('Implement this route')
