import pytest
import requests


BASE_URL = "http://127.0.0.1:5000"

tasks = []

def test_create_task():
    response = requests.post(
        f"{BASE_URL}/tasks",
        json={"title": "Task 1", "description": "Description of task 1"},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Task created successfully"}