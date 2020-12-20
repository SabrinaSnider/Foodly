from models import db


"""Model for grocery products."""
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  publixProductId = db.Column(db.String(64))
  publixAisle = db.Column(db.String(64))
  publixSection = db.Column(db.String(64))
  obtained = db.Column(db.Boolean)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'publixProductId': self.publixProductId,
      'publixAisle': self.publixAisle,
      'publixSection': self.publixSection,
      'obtained': self.obtained
    }
