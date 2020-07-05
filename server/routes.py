from flask import request, render_template
from flask_cors import cross_origin, CORS
from scrapers.Publix import getPublixProductInfo
from helper.pandasOperations import groupByLocation
from flask import Blueprint
from models import db
from models.product import Product
from flask import jsonify

router = Blueprint('routes', __name__,)
CORS(router)

@router.route('/all', methods=['GET'])
def getAllProducts():
  products = Product.query.all()
  jsonUnsoredTable = [i.serialize() for i in products]
  if not jsonUnsoredTable:
    return None
  return jsonify(groupByLocation(jsonUnsoredTable, "publixAisle").to_dict())

@router.route('/add-item', methods=['POST'])
@cross_origin()
def add_item():
  name = request.json['product']
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
@cross_origin()
def delete_item():
  databaseId = request.data
  Product.query.filter_by(id=databaseId).delete()
  
  db.session.commit()
  return "Successfully deleted item"
