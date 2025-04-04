
from app.extraction.json_extractor import JSONExtractor
from app.extraction.csv_extractor import CSVExtractor
from app.extraction.abstract_data_extractor import AbstractDataExtractor

class ExtractorFactory:
    @staticmethod
    def get_extractor(file_type: str) -> AbstractDataExtractor:
        if file_type == "json":
            return JSONExtractor()
        elif file_type == "csv":
            return CSVExtractor()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
