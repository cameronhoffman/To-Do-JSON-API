from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

from controllers import itemlist_controller
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
    body = request.get_json()

    # Right now, this function tries to create an ItemList immediately, but it
    # will fail if the body isn't valid.
    # You need to handle this situation appropriately and exit the function
    # early, return a 422 error code, and include an appropriate message.
    itemlist = itemlist_controller.create_itemlist(body)

    return jsonify(model_to_dict(itemlist)), 201

## Not-Implemented

@app.route('/lists/<listitem_id>')
def get_itemlist(listitem_id):
    """Gets a single itemlist by ID"""
    raise Exception('Implement this route')

@app.route('/lists/<listitem_id>', methods=['PUT'])
def update_itemlist(listitem_id):
    """Updates a single itemlist by ID"""
    raise Exception('Implement this route')

@app.route('/lists/<listitem_id>', methods=['DELETE'])
def delete_itemlist(listitem_id):
    """Deletes a single itemlist by ID"""
    raise Exception('Implement this route')

@app.route('/lists/<listitem_id>/items')
def get_items_by_list(listitem_id):
    """Gets all items for a single list"""
    raise Exception('Implement this route')

@app.route('/items', methods=['POST'])
def create_item():
    """Creates a list based on the request body"""
    raise Exception('Implement this route')

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    """Updates a single item by ID"""
    raise Exception('Implement this route')

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Deletes a single item by ID"""
    raise Exception('Implement this route')
