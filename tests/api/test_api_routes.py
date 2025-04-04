import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fetch_records():
    response = client.get("/records")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_fetch_filtered_records():
    response = client.get("/records/filter?category=HR")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_fetch_insights():
    response = client.get("/records/insights")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_aggregated_role_salary():
    response = client.get("/records/aggregated_role_salary")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_employee_count():
    response = client.get("/records/employee_count")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
