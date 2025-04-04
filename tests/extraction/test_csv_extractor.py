import pytest
from app.extraction.csv_extractor import CSVExtractor
from io import StringIO

def test_csv_extractor_valid():
    csv_data = "name,email\nJohn Doe,john@example.com\nJane Doe,jane@example.com"
    extractor = CSVExtractor()

    extracted_data = list(extractor.extract(StringIO(csv_data).getvalue()))  
    assert len(extracted_data) > 0

def test_csv_extractor_invalid():
    csv_data = "name|email\nJohn Doe|john@example.com"
    extractor = CSVExtractor()
    
    with pytest.raises(ValueError):
        list(extractor.extract(StringIO(csv_data)))