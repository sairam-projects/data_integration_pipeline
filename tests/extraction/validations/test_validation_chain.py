import pytest
from app.extraction.validations.validation_chain import ValidationChain

@pytest.fixture
def validation_chain():
    return ValidationChain()

def test_validation_chain_passes(validation_chain):
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
    assert validation_chain.validate(data) is None

def test_validation_chain_fails(validation_chain):
    data = {"name": None}
    with pytest.raises(ValueError, match="Validation Error: name cannot be null or empty"):
        validation_chain.validate(data)
