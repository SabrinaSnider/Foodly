from models import db


class Product(db.Model):
  """Data model for grocery products."""

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  publixLocation = db.Column(db.String(64))
  obtained = db.Column(db.Boolean)

  def serialize(self):
    """Return object data in easily serializable format"""
    return {
        'id': self.id,
        'name': self.name,
        'publixLocation': self.publixLocation,
        'obtained': self.obtained
    }
