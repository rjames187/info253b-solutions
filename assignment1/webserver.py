from flask import Flask, request
import json

app = Flask(__name__)

db = {}

@app.route('/v1/tasks', methods=['POST'])
def create_task():
  cur_id = len(db) + 1
  data = request.get_json()
  task = {}
  task['title'] = data['title']
  task['is_completed'] = data['is_completed'] if 'is_completed' in data else False
  task['id'] = cur_id
  db[str(cur_id)] = task
  response = { 'id': cur_id }
  cur_id += 1
  return response, 201

@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
  response = { 'tasks': list(db.values()) }
  return response, 200

@app.route('/v1/tasks/<id>', methods=['GET'])
def get_task(id):
  if id in db:
    return db[id], 200
  return { 'error': 'There is no task at that id' }, 404

@app.route('/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  del db[id]
  return {}, 204

@app.route('/v1/tasks/<id>', methods=['PUT'])
def edit_task(id):
  if not id in db:
    return { 'error': 'There is no task at that id' }, 404
  data = request.get_json()
  t = db[id]
  if 'title' in data:
    t['title'] = data['title']
  if 'is_completed' in data:
    t['is_completed'] = data['is_completed']
  return {}, 204
      