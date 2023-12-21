from sqlalchemy import text

class QueryFactory:
  def __init__(self):
    pass
  def create(self, task: dict):
    x = task["title"]
    y = "TRUE" if "is_completed" in task and task["is_completed"] else "FALSE"
    stmt = text(f"INSERT INTO tasks (task, is_completed) VALUES ('{x}', {y})")
    return stmt
  def get_all(self):
    return text("SELECT * FROM tasks")
  def get(self, id: int):
    stmt = text(f"SELECT * FROM tasks WHERE id = {id}")
    return stmt
  def delete(self, id: int):
    stmt = text(f"DELETE FROM tasks WHERE id = {id}")
    return stmt
  def put(self, id: int, data):
    if len(data) == 0:
      return None
    task = data['title']
    is_completed = "TRUE" if data['is_completed'] else "FALSE"
    stmt = text(f"UPDATE tasks SET task = '{task}', SET is_completed = {is_completed} WHERE id = {id}")
    return stmt
    