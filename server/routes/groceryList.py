from flask import request, render_template
from flask_cors import cross_origin, CORS
from scrapers.publix import getPublixProductInfo
from helper.pandasOperations import groupByLocationAndSort
from flask import Blueprint
from models import db
from models.groceryList import GroceryList
from models.product import Product
from flask import jsonify


grocery_list_router = Blueprint('grocery_list_rotues', __name__,)
CORS(grocery_list_router)

@grocery_list_router.route('/create', methods=['POST'])
@cross_origin()
def create():
  if not request.json or 'name' not in request.json: return {'error': 'Invalid name.'}, 500

  name = request.json['name']
  if not name: return {'error': 'Invalid name.'}, 500

  new_list = GroceryList(name="test")
  db.session.add(new_list)
  db.session.commit()
  return f'Created list {name} with id {new_list.id}.'

@grocery_list_router.route('/<id>/products', methods=['GET'])
def getAllProducts(id):
  grocery_list_object = GroceryList.query.get(id)
  if grocery_list_object is None: return {'error': 'Invalid list.'}, 500

  products = grocery_list_object.products
  json_table = [i.serialize() for i in products]
  return {} if not json_table else jsonify(groupByLocationAndSort(json_table, "publixAisle"))

@grocery_list_router.route('/<id>/add-item', methods=['POST'])
@cross_origin()
def add_item(id):
  grocery_list_object = GroceryList.query.get(id)
  if grocery_list_object is None: return {'error': 'Invalid list.'}, 500

  name = request.json['product']
  if not name: return {'error': 'Invalid product.'}, 500

  productInfo = getPublixProductInfo(name)
  new_product = Product(
    name=name,
    publixProductId=productInfo["productId"],
    publixAisle=productInfo["aisle"],
    obtained=False
  )
  if "section" in productInfo: new_product.publixSection = productInfo["section"]

  grocery_list_object.products.append(new_product)
  
  db.session.add(grocery_list_object)
  db.session.commit()
  return jsonify(new_product.serialize())

@grocery_list_router.route('/<listId>/delete-item/<itemId>', methods=['DELETE'])
@cross_origin()
def delete_item(listId, itemId):
  product_to_delete = Product.query.filter(Product.grocery_list_id == listId and Product.id == itemId)
  if product_to_delete is None: return {'error': 'Invalid params.'}, 500

  product_to_delete.delete()
  db.session.commit()
  return "Successfully deleted item"

@grocery_list_router.route('/<listId>/toggle/<itemId>', methods=['POST'])
@cross_origin()
def toggle_item_obtained(listId, itemId):
  product_to_toggle = Product.query.filter(Product.grocery_list_id == listId and Product.id == itemId).first()
  if product_to_toggle is None: return {'error': 'Invalid params.'}, 500

  product_to_toggle.obtained = not product_to_toggle.obtained
  db.session.commit()
  return f'Successfully toggled {product_to_toggle.name} to be ' + str(product_to_toggle.obtained)
