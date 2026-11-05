import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_default_greeting():
    """GET / should return the default greeting."""
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert json_data.get("greeting") == "Hello, World!"


def test_root_custom_greeting():
    """GET / with ?msg=Foo should return the custom greeting."""
    response = client.get("/", params={"msg": "Foo"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("greeting") == "Foo"


def test_health_endpoint():
    """GET /health should return status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("status") == "ok"