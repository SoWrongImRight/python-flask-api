from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Add(Resource):
  pass

class Subtract(Resource):
  pass

class Multiply(Resource):
  pass

class Divide(Resource):
  pass

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__=="__main__":
  app.run(debug=True)