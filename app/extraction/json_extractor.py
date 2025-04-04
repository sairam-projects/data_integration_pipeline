'''
import json
import logging

from app.extraction.data_extractor import DataExtractor

logging.basicConfig(level=logging.INFO)

class JSONExtractor(DataExtractor):
  
  def extract(self, data):
    try:
      result = json.loads(data)
      logging.info("Json data extracted successfully")
      return result
    except Exception as e:
      logging.error("Json extraction failed: %s", e)
      raise ValueError("Error in Json extraction")'''

import json
import logging
from app.extraction.abstract_data_extractor import AbstractDataExtractor

class JSONExtractor(AbstractDataExtractor):
  def extract(self, data, chunk_size=1000):
    try:
      json_data = json.loads(data)
      if isinstance(json_data, dict):
        json_data = [json_data]  # Convert single dict to list

      # Yield data in chunks
      for i in range(0, len(json_data), chunk_size):
        yield json_data[i:i + chunk_size]
    except Exception as e:
      logging.error("JSON extraction failed: %s", e)
      raise ValueError("Invalid JSON format")
