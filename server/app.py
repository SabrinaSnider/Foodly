from flask import Flask, jsonify
from flask_cors import CORS

# To start server:
# $env:FLASK_APP = "app.py"
# $env:FLASK_ENV = "development"
# flask run

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Routes
from PublixScraper import getItemLocation

@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

@app.route('/item/<string:item>')
def itemLocation(item):
  return getItemLocation(item)

if __name__ == '__main__':
    app.run()
