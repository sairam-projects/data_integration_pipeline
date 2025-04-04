'''import csv
import logging
from .data_extractor import DataExtractor

logging.basicConfig(level=logging.INFO)

class CSVExtractor(DataExtractor):
  def extract(self, data):
    try:
      result = []
      reader = csv.reader(data.splitlines())
      for row in reader:
          result.append(row)
      logging.info("CSV extraction successful")
      return result
    except Exception as e:
      logging.error("CSV extraction failed: %s", e)
      raise ValueError("Invalid CSV format")'''

import csv
import logging

from app.extraction.abstract_data_extractor import AbstractDataExtractor

class CSVExtractor(AbstractDataExtractor):
  def extract(self, data, chunk_size=1000):
    try:
      reader = csv.DictReader(data.splitlines())
      batch = []

      for idx, row in enumerate(reader):
        batch.append(row)
      if (idx + 1) % chunk_size == 0:
        yield batch
        batch = []

      # Yield remaining data
      if batch:
        yield batch
    except Exception as e:
      logging.error("CSV extraction failed: %s", e)
      raise ValueError("Invalid CSV format")
