from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
  if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
    if "x" not in postedData or "y" not in postedData:
      return 301
    else:
      return 200
  elif (functionName == "divide"):
    if "x" not in postedData or "y" not in postedData:
      return 301
    elif int(postedData["y"])==0:
      return 302
    else:
      return 200

class Add(Resource):
  def post(self):
    # Step 1, get POSTED data
    postedData=request.get_json()

    status_code = checkPostedData(postedData, "add")
    print(status_code)
    if (status_code!=200):
      retJson = {
        "Message": "An error has occurred",
        "Status Code": status_code
      }
      return jsonify(retJson)


    x=postedData["x"]
    y=postedData["y"]
    x=int(x)
    y=int(y)

    # Step 2, add data
    ret = x+y

    # Return results
    retMap = {
      'Message': ret,
      'Status Code':status_code
    }
    return jsonify(retMap)

class Subtract(Resource):
  def post(self):
    # Step 1, get POSTED data
    postedData=request.get_json()

    status_code = checkPostedData(postedData, "subtract")
    print(status_code)
    if (status_code!=200):
      retJson = {
        "Message": "An error has occurred",
        "Status Code": status_code
      }
      return jsonify(retJson)


    x=postedData["x"]
    y=postedData["y"]
    x=int(x)
    y=int(y)

    # Step 2, subtract data
    ret = x-y

    # Return results
    retMap = {
      'Message': ret,
      'Status Code':status_code
    }
    return jsonify(retMap)

class Multiply(Resource):
  def post(self):
    # Step 1, get POSTED data
    postedData=request.get_json()

    status_code = checkPostedData(postedData, "multiply")
    print(status_code)
    if (status_code!=200):
      retJson = {
        "Message": "An error has occurred",
        "Status Code": status_code
      }
      return jsonify(retJson)


    x=postedData["x"]
    y=postedData["y"]
    x=int(x)
    y=int(y)

    # Step 2, multiply data
    ret = x*y

    # Return results
    retMap = {
      'Message': ret,
      'Status Code':status_code
    }
    return jsonify(retMap)

class Divide(Resource):
  def post(self):
    # Step 1, get POSTED data
    postedData=request.get_json()

    status_code = checkPostedData(postedData, "divide")
    print(status_code)
    if (status_code!=200):
      retJson = {
        "Message": "An error has occurred",
        "Status Code": status_code
      }
      return jsonify(retJson)


    x=postedData["x"]
    y=postedData["y"]
    x=int(x)
    y=int(y)

    # Step 2, add data
    ret = (x*1.0)/y

    # Return results
    retMap = {
      'Message': ret,
      'Status Code':status_code
    }
    return jsonify(retMap)

api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')


""" @app.route('/')
def hello_world():
  return 'Hello, World!'
 """
if __name__=="__main__":
  app.run(debug=True)