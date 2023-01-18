import requests
import json

def test_post():
    r = requests.post('http://localhost:5000/post', json={"key": "key1", "value": "value1"})
    true_content = {"key": "key1", "value": "value1", "message":"success"}

    assert r.json() == true_content

def test_get_1():
    r = requests.get('http://localhost:5000/get/key1')
    true_content = {"value": "value1"}

    assert r.json() == true_content


def test_get_2():
    r = requests.get('http://localhost:5000/get?key=key1')
    true_content = {"value": "value1"}

    assert r.json() == true_content

def test_delete():
    r = requests.delete('http://localhost:5000/delete?key=key1', json={"key": "key1"})
    true_content = {"key": "key1", "message": "success"}

    assert r.json() == true_content