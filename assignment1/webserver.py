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