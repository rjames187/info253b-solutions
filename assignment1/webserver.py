from flask import Flask, request
import json

app = Flask(__name__)

cur_id = 1
db = {
  'tasks': []
}

@app.route('/v1/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  task = {}
  task['title'] = data['title']
  task['is_completed'] = data['is_completed'] if 'is_completed' in data else False
  task['id'] = cur_id
  cur_id += 1
  db['tasks'].append(task)
  return { 'id': task['id'] }, 201

@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
  response = { 'tasks': db['tasks'] }
  return response, 200

@app.route('/v1/tasks/<id>', methods=['GET'])
def get_task(id):
  for t in db['tasks']:
    if t['id'] == id:
      return t, 200
  return { 'error': 'There is no task at that id' }, 404

@app.route('/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  for i in range(len(db['tasks'])):
    t = db['tasks'][i]
    if t['id'] == id:
      db['tasks'].pop(i)
      return None, 204
      