import pytest
from app.extraction.json_extractor import JSONExtractor

def test_json_extractor_valid():
    json_data = '{"name": "John Doe", "email": "john@example.com"}'
    extractor = JSONExtractor()
    extracted_data = list(extractor.extract(json_data))
    
    assert len(extracted_data) == 1
    assert extracted_data[0][0]["name"] == "John Doe"

def test_json_extractor_invalid():
    json_data = "{name: John Doe, email: john@example.com}"
    extractor = JSONExtractor()
    
    with pytest.raises(ValueError):
        list(extractor.extract(json_data))
