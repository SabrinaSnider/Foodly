from store_scrapers.publix import getPublixProductInfo
from helper.pandasOperations import groupByLocationAndSort
from models import db
from models.groceryList import GroceryList
from models.product import Product

INVALID_PARAMS_ERROR = 'Invalid parameters.'

def create(name):
  if not name: raise ValueError(INVALID_PARAMS_ERROR)

  new_list = GroceryList(name="test")
  db.session.add(new_list)
  db.session.commit()
  return f'Created list {name} with id {new_list.id}.'

def delete(listId):
  if not listId: raise ValueError(INVALID_PARAMS_ERROR)
  list_to_delete = GroceryList.query.filter(GroceryList.id == listId)
  if list_to_delete is None: raise ValueError(INVALID_PARAMS_ERROR)

  list_to_delete.delete()
  db.session.add()
  db.session.commit()
  return f'Deleted list with id {list_to_delete.id}.'

def get_lists():
  lists = GroceryList.query.all()
  json_lists = [i.serialize() for i in lists]
  return json_lists

def get_products(listId):
  if not listId: raise ValueError(INVALID_PARAMS_ERROR)
  grocery_list_object = GroceryList.query.get(listId)
  if grocery_list_object is None: raise ValueError(INVALID_PARAMS_ERROR)

  products = grocery_list_object.products
  json_products = [i.serialize() for i in products]
  return {} if not json_products else groupByLocationAndSort(json_products, "publixAisle")

def add_product(listId, product):
  if not listId or not product: raise ValueError(INVALID_PARAMS_ERROR)
  grocery_list_object = GroceryList.query.get(listId)
  if grocery_list_object is None: raise ValueError(INVALID_PARAMS_ERROR)

  productInfo = getPublixProductInfo(product)
  new_product = Product(
    name=product,
    publixProductId=productInfo["productId"],
    publixAisle=productInfo["aisle"],
    obtained=False
  )
  if "section" in productInfo: new_product.publixSection = productInfo["section"]

  grocery_list_object.products.append(new_product)
  
  db.session.add(grocery_list_object)
  db.session.commit()
  return new_product.serialize()

def delete_product(listId, productId):
  if not listId or not productId: raise ValueError(INVALID_PARAMS_ERROR)
  product_to_delete = Product.query.filter(Product.grocery_list_id == listId and Product.id == productId)
  if product_to_delete is None: raise ValueError(INVALID_PARAMS_ERROR)

  product_to_delete.delete()
  db.session.commit()
  return f'Successfully deleted product {productId} from list {listId}'

def toggle_product(listId, productId):
  if not listId or not productId: raise ValueError(INVALID_PARAMS_ERROR)
  product_to_toggle = Product.query.filter(Product.grocery_list_id == listId and Product.id == productId).first()
  if product_to_toggle is None: raise ValueError(INVALID_PARAMS_ERROR)

  product_to_toggle.obtained = not product_to_toggle.obtained
  db.session.commit()
  return f'Successfully toggled {product_to_toggle.name} to be ' + str(product_to_toggle.obtained)
