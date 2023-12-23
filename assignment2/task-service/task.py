from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from redis import Redis
from rq import Queue
from email_job import send_email
import json

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/task-db"
db.init_app(app)

redis_conn = Redis(host='broker', port=6379)
q = Queue(connection=redis_conn)

class Task(db.Model):
  __tablename__ = "tasks"
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  task: Mapped[str] = mapped_column(db.String)
  is_completed: Mapped[bool] = mapped_column(db.Boolean)
  notify: Mapped[str] = mapped_column(db.String)

def map_row_to_dict(row):
  res = {}
  res["id"] = row[0].id
  res["title"] = row[0].task
  res["is_completed"] = row[0].is_completed
  return res

@app.route('/test/<email>', methods=['GET'])
def run_task(email):
  q.enqueue(send_email, "funny@cool.com")
  print('email task was enqueued!')
  return {}, 200


@app.route('/v1/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  if not 'tasks' in data:
    completed = True if "is_completed" in data and data["is_completed"] else False
    email = data["notify"] if "notify" in data else None
    task = Task(
      task=data["title"],
      is_completed=completed,
      notify=email
    )
    db.session.add(task)
    db.session.commit()
    return { "id": task.id }, 201
  res = { "tasks": [] }  
  for t in data['tasks']:
    task = Task(
      task=t["title"],
      is_completed=True if "is_completed" in t and t["is_completed"] else False,
      notify = t["notify"] if "notify" in t else None
    )
    db.session.add(task)
    db.session.commit()
    res['tasks'].append({ "id": task.id })
  return res, 201

  

@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
  tasks = db.session.execute(db.select(Task)).all()
  res = []
  for row in tasks:
    res.append(map_row_to_dict(row))
  return { 'tasks': res }, 200

@app.route('/v1/tasks/<id>', methods=['GET'])
def get_task(id):
  tasks = db.session.execute(db.select(Task).where(Task.id == id)).all()
  if len(tasks) == 0:
    return { 'error': 'There is no task at that id' }, 404
  row = tasks[0]
  return map_row_to_dict(row), 200

@app.route('/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  task = db.get_or_404(Task, id)
  db.session.delete(task)
  db.session.commit()
  return {}, 204

@app.route('/v1/tasks', methods=['DELETE'])
def delete_bulk_task():
  data = request.get_json()
  ids = []
  for obj in data['tasks']:
    ids.append(obj['id'])
  db.session.execute(db.delete(Task).where(Task.id.in_(ids)))
  db.session.commit()
  return {}, 204


@app.route('/v1/tasks/<id>', methods=['PUT'])
def edit_task(id):
  data = request.get_json()
  task = db.session.execute(db.select(Task).where(Task.id == id)).all()
  if not task:
    return { 'error': 'There is no task at that id' }, 404
  task_name = data["title"]
  completed = data["is_completed"]
  db.session.execute(db.update(Task).where(Task.id == id).values(task=task_name, is_completed=completed))
  db.session.commit()
  return {}, 204
      