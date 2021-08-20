from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
  return "I just hit /hithere"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
  # Get the two numbers from the posted data
  dataDict = request.get_json()
  x = dataDict["x"]
  y = dataDict["y"]
  
  # Add the two numbers together
  z = x+y
  # Create the JSON to return
  retJson = {
    "z":z
  }
  # Return the jsonify'd JSON
  return jsonify(retJson), 200

@app.route('/bye')
def bye():

  retJson = {
    'Name':'Jack',
    'Age':41,
    'Phones':[
      {
        'phoneName':'S9',
        'phoneNumber':5551212
      },
      {
        'phoneName':'s7',
        'phoneNumber':5551313
      }
    ]
  }

  return jsonify(retJson)

if __name__=="__main__":
  app.run()