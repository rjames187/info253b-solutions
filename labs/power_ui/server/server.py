from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
  num1 = int(request.args.get('num1'))
  num2 = int(request.args.get('num2'))
  answer = num1 + num2
  return { "answer": answer }

@app.route('/sub', methods=['POST'])
def sub():
  data = request.form
  answer = int(data["num1"]) - int(data["num2"])
  return { "answer": answer }

@app.route('/mult', methods=['POST'])
def mult():
  data = request.get_json()
  answer = int(data["num1"]) * int(data["num2"])
  return { "answer": answer }

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response