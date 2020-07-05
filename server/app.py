from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import router
from models import db


# To start server:
# $env:FLASK_APP = "app.py"
# $env:FLASK_ENV = "development"
# flask run

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
  app.register_blueprint(router)

  return app

# initialize app
app = create_app()

if __name__ == '__main__':
    app.run()
