from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
  data = request.get_json()
  answer = data["num1"] + data["num2"]
  return { "answer": answer }

@app.route('/sub', methods=['POST'])
def sub():
  data = request.get_json()
  answer = data["num1"] - data["num2"]
  return { "answer": answer }

@app.route('/mult', methods=['POST'])
def mult():
  data = request.get_json()
  answer = data["num1"] * data["num2"]
  return { "answer": answer }