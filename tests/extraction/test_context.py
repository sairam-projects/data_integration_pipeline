import pytest
import os
from unittest.mock import patch, MagicMock
from app.extraction.context import DataIntegrationContext, run_extraction

@pytest.fixture
def mock_extractor():
    """Mock extractor for simulating extraction behavior."""
    mock = MagicMock()
    mock.extract.return_value = [{"name": "John Doe", "email": "john@example.com"}]
    return mock

@patch("app.extraction.context.ExtractorFactory.get_extractor")
@patch("builtins.open", new_callable=MagicMock)
def test_execute_extraction(mock_open, mock_get_extractor, mock_extractor):
    """Test execution of extraction logic."""
    mock_get_extractor.return_value = mock_extractor
    mock_open.return_value.__enter__.return_value.read.return_value = "mock file data"

    context = DataIntegrationContext("csv")
    results = context.execute_extraction("test.csv")

    assert len(results) == 1
    assert results[0]["name"] == "John Doe"
    mock_extractor.extract.assert_called_once()

@patch("app.extraction.context.DataIntegrationContext.execute_extraction")
def test_run_extraction(mock_execute_extraction):
    """Test run_extraction function."""
    mock_execute_extraction.return_value = [{"name": "Jane Doe", "email": "jane@example.com"}]

    results = run_extraction("test.csv", "csv")

    assert len(results) == 1
    assert results[0]["name"] == "Jane Doe"
    mock_execute_extraction.assert_called_once_with("test.csv")