from store_scrapers.publix import get_product_info
from helper.sorting import organize_list
from models import db
from models.GroceryList import GroceryList
from models.Product import Product


INVALID_PARAMS_ERROR = 'Invalid parameters.'

def create(name):
  if not name: raise ValueError(INVALID_PARAMS_ERROR)

  new_list = GroceryList(name="test")
  db.session.add(new_list)
  db.session.commit()
  return f'Created list {name} with id {new_list.id}.'

def delete(list_id):
  if not list_id: raise ValueError(INVALID_PARAMS_ERROR)
  list_to_delete = GroceryList.query.filter(GroceryList.id == list_id)
  if list_to_delete is None: raise ValueError(INVALID_PARAMS_ERROR)

  list_to_delete.delete()
  db.session.commit()
  return 'Deleted list.'

def get_lists():
  lists = GroceryList.query.all()
  json_lists = [i.serialize() for i in lists]
  return json_lists

def get_products(list_id):
  if not list_id: raise ValueError(INVALID_PARAMS_ERROR)
  grocery_list_object = GroceryList.query.get(list_id)
  if grocery_list_object is None: raise ValueError(INVALID_PARAMS_ERROR)

  products = grocery_list_object.products
  json_products = [i.serialize() for i in products]
  return {} if not json_products else organize_list(json_products, "publix_aisle")

def add_product(list_id, product):
  if not list_id or not product: raise ValueError(INVALID_PARAMS_ERROR)
  grocery_list_object = GroceryList.query.get(list_id)
  if grocery_list_object is None: raise ValueError(INVALID_PARAMS_ERROR)

  product_info = get_product_info(product)
  new_product = Product(
    name=product,
    publix_aisle=product_info["aisle"],
    obtained=False
  )
  if "section" in product_info: new_product.publixSection = product_info["section"]

  grocery_list_object.products.append(new_product)
  
  db.session.add(grocery_list_object)
  db.session.commit()
  return new_product.serialize()

def delete_product(list_id, product_id):
  if not list_id or not product_id: raise ValueError(INVALID_PARAMS_ERROR)
  product_to_delete = Product.query.filter(Product.grocery_list_id == list_id).filter(Product.id == product_id)
  if product_to_delete is None: raise ValueError(INVALID_PARAMS_ERROR)

  product_to_delete.delete()
  db.session.commit()
  return 'Deleted product from list {list_id}'

def toggle_product(list_id, product_id):
  if not list_id or not product_id: raise ValueError(INVALID_PARAMS_ERROR)
  product_to_toggle = Product.query.filter(Product.grocery_list_id == list_id).filter(Product.id == product_id).first()
  if product_to_toggle is None: raise ValueError(INVALID_PARAMS_ERROR)

  product_to_toggle.obtained = not product_to_toggle.obtained
  db.session.commit()
  return f'Successfully toggled {product_to_toggle.name} to be ' + str(product_to_toggle.obtained)
