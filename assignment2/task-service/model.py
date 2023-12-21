from sqlalchemy import text

class QueryFactory:
  def __init__(self):
    pass
  def create(self, task: dict):
    x = task["title"]
    y = "TRUE" if "is_completed" in task and task["is_completed"] else "FALSE"
    stmt = text("INSERT INTO tasks (task, is_completed) VALUES (:x, :y)")
    stmt = stmt.bind_params(x=x, y=y)
    return stmt
  def get_all(self):
    return text("SELECT * FROM tasks")
  def get(self, id: int):
    stmt = text("SELECT * FROM tasks WHERE id = :x")
    stmt = stmt.bind_params(x=id)
    return stmt
  def delete(self, id: int):
    stmt = text("DELETE FROM tasks WHERE id = :x")
    stmt = stmt.bind_params(x=id)
    return stmt
  def put(self, id: int, data):
    if len(data) == 0:
      return None
    task = data['title']
    is_completed = data['is_completed']
    stmt = text("UPDATE tasks SET task = :x, SET is_completed = :y WHERE id = :z")
    stmt.bind_params(x=task, y=is_completed, z=id)
    return stmt
    