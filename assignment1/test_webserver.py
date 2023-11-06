import requests
import json

def test_create_task():
    r = requests.post('http://localhost:5000/v1/tasks', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1

def test_list_all_tasks():
    r = requests.get('http://localhost:5000/v1/tasks')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3

def test_get_task():
    r = requests.get('http://localhost:5000/v1/tasks/1')
    assert isinstance(r.json(),dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3

def test_update_task():
    r = requests.put('http://localhost:5000/v1/tasks/1', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content

def test_get_updated_task():
    r = requests.get('http://localhost:5000/v1/tasks/1')
    assert r.json()["is_completed"]

def test_delete_task():
    r = requests.delete('http://localhost:5000/v1/tasks/1')
    assert not r.content

def test_get_missing_task():
    r = requests.get('http://localhost:5000/v1/tasks/1')
    assert r.status_code == 404

def test_edit_missing_task():
    r = requests.put('http://localhost:5000/v1/tasks/1', json={})
    assert r.status_code == 404

def test_bulk_create_tasks():
    data = {
            "tasks": [
                {"title": "Test Task 1", "is_completed": True},
                {"title": "Test Task 2", "is_completed": False},
                {"title": "Test Task 3", "is_completed": True}
            ]
        }
    r = requests.post('http://localhost:5000/v1/tasks', json=data)
    res = r.json()
    assert isinstance(res, dict)
    assert isinstance(res['tasks'], list)
    assert isinstance(res['tasks'][0], dict)
    assert isinstance(res['tasks'][0]['id'], int)
    assert len(res['tasks']) == 3

def test_list_all_tasks_again():
    r = requests.get('http://localhost:5000/v1/tasks')
    assert len(r.json()['tasks']) == 3

def delete_bulk_tasks():
    data = {
        'tasks': [
            { 'id': 1 },
            { 'id': 2 },
            { 'id': 3 }
        ]
    }
    r = requests.delete('http://localhost:5000/v1/tasks', json=data)
    assert not r.content

def list_deleted_tasks():
    r = requests.get('http://localhost:5000/v1/tasks')
    assert len(r.json()['tasks']) == 0

