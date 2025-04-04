import pytest
from app.extraction.validations.not_null_validation import NotNullValidator

@pytest.fixture
def not_null_validator():
    return NotNullValidator()

def test_valid_data(not_null_validator):
    data = {"name": "John Doe", "email": "john@example.com"}
    assert not_null_validator.do_validate(data) is None

def test_missing_required_field(not_null_validator):
    data = {"name": "John Doe"}
    with pytest.raises(ValueError, match="Validation Error: email cannot be null or empty"):
        not_null_validator.do_validate(data)
