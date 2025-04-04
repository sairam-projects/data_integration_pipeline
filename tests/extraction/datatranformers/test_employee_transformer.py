import json
import pytest
from app.extraction.datatranformers.employee_transformer import transform_with_extra_data

def test_transform_with_all_fields():
    record = {
        "name": "John Doe",
        "organization": "TechCorp",
        "email": "john@example.com",
        "department": "Engineering",
        "role": "Developer",
        "hire_date": "2023-05-10",
        "salary": 75000,
        "source_type": "csv",
        "timestamp": "2023-05-10T12:00:00",
        "extra_field1": "extra_value1",
        "extra_field2": "extra_value2"
    }

    transformed = transform_with_extra_data(record)
    
    assert transformed["name"] == "John Doe"
    assert transformed["email"] == "john@example.com"
    assert transformed["extra_data"] == json.dumps({"extra_field1": "extra_value1", "extra_field2": "extra_value2"})

def test_transform_with_no_extra_fields():
    record = {
        "name": "Jane Doe",
        "organization": "HealthCorp",
        "email": "jane@example.com",
        "department": "HR",
        "role": "Manager",
        "hire_date": "2022-08-15",
        "salary": 90000,
        "source_type": "json",
        "timestamp": "2022-08-15T10:30:00"
    }

    transformed = transform_with_extra_data(record)

    assert transformed["name"] == "Jane Doe"
    assert transformed["extra_data"] is None

def test_transform_with_empty_record():
    record = {}

    transformed = transform_with_extra_data(record)

    assert transformed["name"] is None
    assert transformed["extra_data"] is None

def test_transform_with_partial_fields():
    record = {
        "name": "Alice",
        "email": "alice@example.com",
        "random_field": "random_value"
    }

    transformed = transform_with_extra_data(record)

    assert transformed["name"] == "Alice"
    assert transformed["email"] == "alice@example.com"
    assert transformed["extra_data"] == json.dumps({"random_field": "random_value"})
