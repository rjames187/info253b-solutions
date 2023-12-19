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
  if task and 'task' in task:
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
    result = polish(result)
    return json.dumps(result[0]), 201
  res = []
  for t in data['tasks']:
    stmt = qf.create(t)
    result = db.session.execute(stmt).all()
    result = polish(result)
    res.append(result)
  return { 'tasks': res }, 201

@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
  stmt = qf.get_all()
  result = db.session.execute(stmt).all()
  response = { 'tasks': polish(result) }
  return response, 200

@app.route('/v1/tasks/<id>', methods=['GET'])
def get_task(id):
  stmt = qf.get(id)
  result = db.session.execute(stmt).all()
  if not result:
    return { 'error': 'There is no task at that id' }, 404
  return polish(result), 200

@app.route('/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  stmt = qf.delete(id)
  db.session.execute(stmt).all()
  return {}, 204

@app.route('/v1/tasks', methods=['DELETE'])
def delete_bulk_task():
  data = request.get_json()
  for obj in data['tasks']:
    stmt = qf.delete(obj['id'])
    db.session.execute(stmt).all()
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
      