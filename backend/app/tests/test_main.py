from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health_check")

    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_hello_world():
    response = client.get("/hello_world")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_add_endpoint():
    response = client.post("/add", json={"nums": [1, 2, 3]})

    assert response.status_code == 200
    assert response.json() == {"result": 6}
