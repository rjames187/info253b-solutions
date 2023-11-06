from flask import Flask, request
import json
from model import database

app = Flask(__name__)

model = database()

@app.route('/v1/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  response = model.add_task(data)
  return response, 201

@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
  db = model.db
  response = { 'tasks': list(db.values()) }
  return response, 200

@app.route('/v1/tasks/<id>', methods=['GET'])
def get_task(id):
  db = model.db
  if id in db:
    return db[id], 200
  return { 'error': 'There is no task at that id' }, 404

@app.route('/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  model.delete_task(id)
  return {}, 204

@app.route('/v1/tasks/<id>', methods=['PUT'])
def edit_task(id):
  db = model.db
  if not id in db:
    return { 'error': 'There is no task at that id' }, 404
  data = request.get_json()
  t = db[id]
  if 'title' in data:
    t['title'] = data['title']
  if 'is_completed' in data:
    t['is_completed'] = data['is_completed']
  return {}, 204
      