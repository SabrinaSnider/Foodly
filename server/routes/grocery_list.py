from flask import request, render_template
from flask_cors import cross_origin, CORS
from flask import Blueprint
from flask import jsonify
from services.grocery_list import *


grocery_list_router = Blueprint('grocery_list_rotues', __name__,)
CORS(grocery_list_router)

@grocery_list_router.route('/create', methods=['POST'])
@cross_origin()
def create_endpoint():
  if not request.json or 'name' not in request.json: return {'error': 'Invalid name.'}, 500
  try:
    data = create(request.json['name'])
    return data
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<list_id>/delete', methods=['DELETE'])
@cross_origin()
def delete_endpoint(list_id):
  try:
    data = delete(list_id)
    return data
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/get-lists', methods=['GET'])
def get_lists_endpoint():
  try:
    data = get_lists()
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<list_id>', methods=['GET'])
def get_list_endpoint(list_id):
  try:
    data = get_list(list_id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<list_id>/add-product', methods=['POST'])
@cross_origin()
def add_product_endpoint(list_id):
  if not request.json or 'product' not in request.json: return {'error': 'Invalid product name.'}, 500
  try:
    data = add_product(list_id, request.json['product'])
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<list_id>/delete-product/<item_id>', methods=['DELETE'])
@cross_origin()
def delete_product_endpoint(list_id, item_id):
  try:
    data = delete_product(list_id, item_id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<list_id>/toggle-product/<item_id>', methods=['POST'])
@cross_origin()
def toggle_product_endpoint(list_id, item_id):
  try:
    data = toggle_product(list_id, item_id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500
