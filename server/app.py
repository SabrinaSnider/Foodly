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
  app.config.from_object('config.Config')

  # enable CORS
  CORS(app, resources={r'/*': {'origins': '*'}})

  # initialize database
  db.init_app(app)

  # Import routes
  app.register_blueprint(router)

  #db.create_all()  # Create sql tables for our data models

  return app

# initialize app
app = create_app()

if __name__ == '__main__':
    app.run()
