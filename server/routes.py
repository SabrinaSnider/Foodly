from flask import request, render_template
from scrapers.Publix import getItemLocation
from flask import Blueprint
from models import db
from models.product import Product

router = Blueprint('routes', __name__,)

@router.route('/ping', methods=['GET'])
def ping_pong():
  return 'pong!'

@router.route('/item/<string:item>')
def itemLocation(item):
  return getItemLocation(item)

# @router.route('/setdata', methods=['GET'])
# def user_records():
#   new_product = Product(
#     name="cheerios",
#     locaiton="filler",
#     obtained=False
#   )
#   db.session.add(new_product)  # Adds new User record to database
#   db.session.commit()  # Commits all changes
#   return "product successfully created!"