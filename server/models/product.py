from models import db


class Product(db.Model):
  """Data model for user accounts."""

  __tablename__ = 'products'
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  name = db.Column(
    db.String(64),
    index=False,
    unique=True,
    nullable=False
  )
  publixLocation = db.Column(
    db.String(64),
    index=False,
    unique=False,
    nullable=True
  )
  obtained = db.Column(
    db.Boolean,
    index=False,
    unique=False,
    nullable=False
  )

