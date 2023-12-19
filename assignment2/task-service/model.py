from sqlalchemy import text

class QueryFactory:
  def __init__(self):
    pass
  def create(task: dict):
    x = task["title"]
    y = "TRUE" if task["is_completed"] else "FALSE"
    stmt = text("INSERT INTO tasks (task, is_completed) VALUES (:x, :y)")
    stmt = stmt.bind_params(x=x, y=y)
    return stmt
  def get_all():
    return text("SELECT * FROM tasks")
  def get(id: int):
    stmt = text("SELECT * FROM tasks WHERE id = :x")
    stmt = stmt.bind_params(x=id)
    return stmt