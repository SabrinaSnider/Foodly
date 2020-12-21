from models import db


"""Model for grocery lists."""
class GroceryList(db.Model):
  __tablename__ = 'GroceryList'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  products = db.relationship('Product', backref='GroceryList')

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'products': [i.serialize() for i in self.products],
    }
