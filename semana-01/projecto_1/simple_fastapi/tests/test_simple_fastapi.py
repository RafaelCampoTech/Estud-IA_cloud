import pytest
from fastapi.testclient import TestClient

from function import dummy_function
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Grupo Estud-IA"}


def test_read_item():
    response = client.get("/items/7", params={"q": "week"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 7, "q": "week"}


def test_read_item_without_query():
    response = client.get("/items/3")
    assert response.status_code == 200
    assert response.json() == {"item_id": 3, "q": None}


def test_read_dummy_default():
    response = client.get("/dummy")
    assert response.status_code == 200
    assert response.json() == {"a": "Dummy", "message": "Hello from dummy_function!"}


def test_read_dummy_with_query():
    response = client.get("/dummy", params={"a": "other"})
    assert response.status_code == 200
    assert response.json() == {"a": "other", "message": "Hello from dummy_function!"}


def test_dummy_function_default_returns_greeting():
    assert dummy_function() == "Hello from dummy_function!"


def test_dummy_function_explicit_dummy_returns_greeting():
    assert dummy_function("Dummy") == "Hello from dummy_function!"


def test_dummy_function_other_value_raises():
    with pytest.raises(ValueError, match="a is not Dummy"):
        dummy_function("other")
