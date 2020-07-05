from flask import request, render_template
from scrapers.Publix import getItemLocation
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
  return jsonify([i.serialize() for i in products])

@router.route('/add-item', methods=['POST'])
def add_item():
  product = request.json["product"]
  location = getItemLocation(product)

  new_product = Product(
    name=product,
    publixLocation=location["location"],
    obtained=False
  )

  if "section" in location:
    new_product.publixSection = location["section"]

  db.session.add(new_product)
  db.session.commit()
  return "Added " + product + " with location " + location["location"]
