class database:
  def __init__(self):
    self.db = {}
  def add_task(self, data):
    cur_id = len(self.db) + 1
    task = {}
    task['title'] = data['title']
    task['is_completed'] = data['is_completed'] if 'is_completed' in data else False
    task['id'] = cur_id
    self.db[str(cur_id)] = task
    return { 'id': cur_id }
  def delete_task(self, id):
    del self.db[id]
  
