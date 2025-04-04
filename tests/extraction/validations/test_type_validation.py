import pytest
from app.extraction.validations.type_validation import TypeValidation

@pytest.fixture
def type_validator():
    return TypeValidation()

def test_valid_data(type_validator):
    data = {
        "name": "John Doe",
        "organization": "TechCorp",
        "email": "john@example.com",
        "department": "Engineering",
        "role": "Developer",
        "source_type": "csv",
        "hire_date": "2023-05-10",
        "salary": 75000,
        "timestamp": "2023-05-10T12:00:00"
    }
    assert type_validator.do_validate(data) is None  # Should pass without exceptions

def test_invalid_name_type(type_validator):
    data = {"name": 123}  # Invalid name
    with pytest.raises(TypeError, match="Validation Error: name must be a string"):
        type_validator.do_validate(data)

def test_invalid_salary_type(type_validator):
    data = {"salary": "high"}  # Invalid salary type
    with pytest.raises(TypeError, match="Validation Error: salary must be a number or numeric string"):
        type_validator.do_validate(data)
