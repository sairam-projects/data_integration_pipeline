import pytest
from app.extraction.extractor_factory import ExtractorFactory
from app.extraction.json_extractor import JSONExtractor
from app.extraction.csv_extractor import CSVExtractor

def test_extractor_factory_json():
    extractor = ExtractorFactory.get_extractor("json")
    assert isinstance(extractor, JSONExtractor)

def test_extractor_factory_csv():
    extractor = ExtractorFactory.get_extractor("csv")
    assert isinstance(extractor, CSVExtractor)

def test_extractor_factory_invalid():
    with pytest.raises(ValueError):
        ExtractorFactory.get_extractor("xml")
