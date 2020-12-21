from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes.groceryList import grocery_list_router
from models import db


def create_app():
  app = Flask(__name__)

  # enable CORS
  CORS(app)
  app.config['CORS_HEADERS'] = 'Content-Type'

  # initialize database
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.init_app(app)

  # Create sql tables for our data models
  with app.app_context():
    db.create_all()
  
  # import routes
  app.register_blueprint(grocery_list_router, url_prefix="/lists")

  return app

# initialize app
app = create_app()

if __name__ == '__main__':
  app.run()
