from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
  return "I just hit /hithere"

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