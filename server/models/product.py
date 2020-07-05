from models import db


class Product(db.Model):
  """Data model for grocery products."""

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  publixProductId = db.Column(db.String(64))
  publixAisle = db.Column(db.String(64))
  publixSection = db.Column(db.String(64))
  obtained = db.Column(db.Boolean)

  def serialize(self):
    """Return object data in easily serializable format"""
    return {
      'id': self.id,
      'name': self.name,
      'publixProductId': self.publixProductId,
      'publixAisle': self.publixAisle,
      'publixSection': self.publixSection,
      'obtained': self.obtained
    }
