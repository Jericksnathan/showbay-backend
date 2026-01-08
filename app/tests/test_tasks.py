from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing create endpoint"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Task"


def test_get_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Get Task",
            "description": "Testing get endpoint"
        }
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old Title",
            "description": "Old Description"
        }
    )
    task_id = create_response.json()["id"]

    update_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "New Title",
            "description": "New Description"
        }
    )
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "New Title"


def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete Task",
            "description": "Testing delete endpoint"
        }
    )
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
