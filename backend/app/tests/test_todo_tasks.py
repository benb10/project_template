import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


task_data = {
    "title": "Test Task",
    "status": "not_started",
}

updated_task_data = {
    "title": "Updated Test Task",
    "status": "in_progress",
}

partial_update_data = {
    "status": "done",
}


@pytest.fixture
def test_task():
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    return response.json()


# @pytest.mark.django_db
def test_create_task():
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == task_data["title"]
    assert response_data["status"] == task_data["status"]
    assert "id" in response_data


# @pytest.mark.django_db
def test_list_tasks():  # test_task):
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 0


# @pytest.mark.django_db
def test_retrieve_task(test_task):
    task = test_task
    task_id = task["id"]
    response = client.get(f"/tasks/{task_id}/")
    assert response.status_code == 200
    retrieved_task = response.json()
    assert retrieved_task["title"] == task_data["title"]
    assert retrieved_task["status"] == task_data["status"]


# @pytest.mark.django_db
def test_patch_task(test_task):
    task = test_task
    task_id = task["id"]

    # Perform PATCH request to update all fields
    response = client.patch(f"/tasks/{task_id}/", json=updated_task_data)
    assert response.status_code == 200
    updated_task = response.json()

    # Assert that both title and status are updated
    assert updated_task["title"] == updated_task_data["title"]
    assert updated_task["status"] == updated_task_data["status"]


# @pytest.mark.django_db
def test_delete_task(test_task):
    task = test_task
    task_id = task["id"]
    response = client.delete(f"/tasks/{task_id}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

    # Verify task no longer exists
    response = client.get(f"/tasks/{task_id}/")
    assert response.status_code == 404
