from flask import request, render_template
from scrapers.Publix import getPublixProductInfo
from helper.pandasOperations import groupByLocation
from flask import Blueprint
from models import db
from models.product import Product
from flask import jsonify

router = Blueprint('routes', __name__,)

@router.route('/ping', methods=['GET'])
def ping_pong():
  return 'pong!'

@router.route('/all', methods=['GET'])
def getAllProducts():
  products = Product.query.all()
  jsonUnsoredTable = [i.serialize() for i in products]
  if not jsonUnsoredTable:
    return None
  return jsonify(groupByLocation(jsonUnsoredTable, "publixAisle").to_dict())

@router.route('/add-item', methods=['POST'])
def add_item():
  name = request.json["product"]
  productInfo = getPublixProductInfo(name)

  new_product = Product(
    name=name,
    publixProductId=productInfo["productId"],
    publixAisle=productInfo["aisle"],
    obtained=False
  )

  if "section" in productInfo:
    new_product.publixSection = productInfo["section"]
  
  db.session.add(new_product)
  db.session.commit()
  return jsonify(new_product.serialize())

@router.route('/delete-item', methods=['DELETE'])
def delete_item():
  databaseId = request.json["id"]
  Product.query.filter_by(id=databaseId).delete()
  
  db.session.commit()
  return "Successfully deleted item"
