from flask import request, render_template
from flask_cors import cross_origin, CORS
from flask import Blueprint
from flask import jsonify
from services.groceryList import create, delete, get_lists, get_products, add_product, delete_product, toggle_product


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

@grocery_list_router.route('/<listId>/delete', methods=['DELETE'])
@cross_origin()
def delete_endpoint(listId):
  try:
    data = delete(listId)
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

@grocery_list_router.route('/<id>/products', methods=['GET'])
def get_products_endpoint(id):
  try:
    data = get_products(id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<id>/add-product', methods=['POST'])
@cross_origin()
def add_product_endpoint(id):
  try:
    data = add_product(id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<listId>/delete-product/<itemId>', methods=['DELETE'])
@cross_origin()
def delete_product_endpoint(listId, itemId):
  try:
    data = delete_product(id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500

@grocery_list_router.route('/<listId>/toggle-product/<itemId>', methods=['POST'])
@cross_origin()
def toggle_product_endpoint(listId, itemId):
  try:
    data = toggle_product(id)
    return jsonify(data)
  except ValueError as e:
    return {'error': str(e)}, 500
