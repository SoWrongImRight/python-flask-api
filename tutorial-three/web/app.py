"""
Registration of a User
Each user gets ten tokens
Store a sentence on our database for one token
Retrive stored sentence for one token
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]

def verifyPw(username, password):
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find({
        "Username":username
    })[0]["Tokens"]
    return tokens

class Register(Resource):
    def post(self):
        # Step one: get posted data by the users
        postedData = request.get_json()

        # Get the database
        username = postedData["username"]
        password = postedData["password"]

        # Hash(password + salt) = stored password
        hashed_pw = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())

        # Store usernaem and password into database
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens":6
        })

        retJson ={
            "status":200,
            "msg":"You successfully signed up for the API"
        }
        return jsonify(retJson)

class Store(Resource):
    def post(self):
        # Step 1 get posted database
        postedData = request.get_json()

        # Read the database
        username = postedData['username']
        password = postedData['password']
        sentence = postedData['sentence']

        # Step 3 verify username and password matfch
        correct_password = verifyPw(username,password)

        if not correct_password:
            retJson = {
                "status":302
            }
            return jsonify(retJson)

        # Step 4 verify user has tokens
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status":301
            }
            return jsonify(retJson)

        # Step 5 store the sentence and return 200
        users.update({"Username":username},{"$set":{
            "Sentence":sentence,
            "Tokens":num_tokens - 1
        }})
        retJson = {
            "status":200,
            "msg":"Sentence saved successfully"
        }
        return jsonify(retJson)

class Get(Resource):
    def post(self):
        postedData = request.get_json()

        # Read the database
        username = postedData['username']
        password = postedData['password']
        # sentence = postedData['sentence']

        # Step 3 verify username and password match
        correct_password = verifyPw(username,password)

        if not correct_password:
            retJson = {
                "status":302
            }
            return jsonify(retJson)

        # Step 4 verify user has tokens
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status":301
            }
            return jsonify(retJson)

        sentence = users.find({
            "Username": username
        })[0]["Sentence"]

        retJson = {
            "status":200,
            "sentence":str(sentence)
        }

        return jsonify(retJsons)

api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__=="__main__":
    app.run(host='0.0.0.0')

"""
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users':0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{'num_of_users':new_num}})
        return str("Hello user " + str(new_num))

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
api.add_resource(Visit, '/hello')



@app.route('/')
def hello_world():
  return 'Hello, World!'
"""
if __name__=="__main__":
  app.run(host='0.0.0.0')
