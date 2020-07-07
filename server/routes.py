from flask import request, render_template
from flask_cors import cross_origin, CORS
from scrapers.Publix import getPublixProductInfo
from helper.pandasOperations import groupByLocationAndSort
from flask import Blueprint
from models import db
from models.product import Product
from flask import jsonify

router = Blueprint('routes', __name__,)
CORS(router)

@router.route('/all', methods=['GET'])
def getAllProducts():
  products = Product.query.all()
  jsonTable = [i.serialize() for i in products]
  if not jsonTable:
    return None
  return jsonify(groupByLocationAndSort(jsonTable, "publixAisle"))

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

@router.route('/delete-item/<databaseId>', methods=['DELETE'])
@cross_origin()
def delete_item(databaseId):
  Product.query.filter_by(id=databaseId).first().delete()
  
  db.session.commit()
  return "Successfully deleted item"

@router.route('/toggle-item-obtained/<databaseId>', methods=['POST'])
@cross_origin()
def toggle_item_obtained(databaseId):
  product = Product.query.filter_by(id=databaseId).first()
  product.obtained = not product.obtained
  
  db.session.commit()
  return "Successfully toggled item obtained to " + str(product.obtained)
