from models import db


class Product(db.Model):
  """Data model for grocery products."""

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  publixLocation = db.Column(db.String(64))
  obtained = db.Column(db.Boolean)

