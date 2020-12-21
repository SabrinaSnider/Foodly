from models import db


"""Model for grocery products."""
class Product(db.Model):
  __tablename__ = 'Product'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  grocery_list_id = db.Column(db.Integer, db.ForeignKey('GroceryList.id'))
  obtained = db.Column(db.Boolean)

  publixProductId = db.Column(db.String(64))
  publixAisle = db.Column(db.String(64))
  publixSection = db.Column(db.String(64))
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'publixProductId': self.publixProductId,
      'publixAisle': self.publixAisle,
      'publixSection': self.publixSection,
      'obtained': self.obtained
    }
