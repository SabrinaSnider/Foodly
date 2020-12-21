from models import db


"""Model for grocery products."""
class Product(db.Model):
  __tablename__ = 'Product'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  grocery_list_id = db.Column(db.Integer, db.ForeignKey('GroceryList.id'))
  obtained = db.Column(db.Boolean)

  publix_aisle = db.Column(db.String(64))
  publix_section = db.Column(db.String(64))
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'publix_aisle': self.publix_aisle,
      'publix_section': self.publix_section,
      'obtained': self.obtained
    }
