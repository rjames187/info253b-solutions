from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from model import QueryFactory
import json

qf = QueryFactory()
app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/task-db"
db.init_app(app)

# renames 'task' column to 'title'
def polish(task):
  if 'task' in task:
    title = task['task']
    del task['task']
    task['title'] = title
  return task

@app.route('/v1/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  if not 'tasks' in data:
    stmt = qf.create(data)
    result = db.session.execute(stmt).all()
    return json.dumps(result[0]), 201
  res = []
  for t in data['tasks']:
    stmt = qf.create(t)
    result = db.session.execute(stmt).all()
    res.append(result)
  return { 'tasks': res }, 201

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

@app.route('/v1/tasks', methods=['DELETE'])
def delete_bulk_task():
  data = request.get_json()
  for obj in data['tasks']:
    model.delete_task(obj['id'])
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
      