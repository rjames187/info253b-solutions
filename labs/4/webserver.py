from flask import Flask, request
import json

app = Flask(__name__)

db = {}

def add_to_db(data, db):
    key = data["key"]
    value = data["value"]
    db[key] = value

def get_from_db(key, db):
    if key not in db:
        return { "message": "key not found" }, 404
    response = { "value": db[key] }
    return json.dumps(response), 200

@app.route('/post', methods = ['POST'])
def post():
    data = request.get_json()
    add_to_db(data, db)
    data["message"] = "success"
    return json.dumps(data), 200

@app.route('/get/<key>')
def key(key):
    return get_from_db(key, db)

@app.route('/get', methods = ['GET'])
def key_get():
    key = request.args.get("key")
    return get_from_db(key, db)

@app.route('/delete', methods = ['DELETE'])
def delete():
    data = request.get_json()
    key = data["key"]
    if key not in db:
        return { "message": "key not found" }, 404
    del db[key]
    response = {"key": key, "message": "success"}
    return json.dumps(response), 200


