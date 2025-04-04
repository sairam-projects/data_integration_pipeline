import os
import logging
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from app.extraction.db_operations.insert_data import DataInserter
from app.extraction.extractor_factory import ExtractorFactory
from app.extraction.validations.validation_chain import ValidationChain
from app.extraction.datatranformers.employee_transformer import transform_with_extra_data

DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)),"..","data")

logging.basicConfig(level=logging.INFO)

def process_chunk(chunk):
  logging.info(f"Processing chunk of size {len(chunk)}")
  return chunk

class DataIntegrationContext:
  def __init__(self, file_type: str):
    self.extractor = ExtractorFactory.get_extractor(file_type)

  def execute_extraction(self,file_name,chunk_size=100000, max_workers=8):
    results = []

    try:
      file_path = os.path.join(DATA_FOLDER, file_name)
      with open(file_path) as f:
        data = f.read()
        #return self.extractor.extract(data)
      
      with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [
        executor.submit(process_chunk, chunk)
        for chunk in self.extractor.extract(data, chunk_size)
        ]

        for future in concurrent.futures.as_completed(futures):
          results.extend(future.result())

      return results
    except ValueError as ve:
      logging.error("Extraction error: %s", ve)
      raise
    except FileNotFoundError as fne:
      logging.error("Extraction error: %s", fne)
      raise
    except Exception as e:
      logging.critical("Unexpected error during extraction: %s", e)
      raise

def run_extraction(file_name,file_type):
    extractor = DataIntegrationContext(file_type)
    return extractor.execute_extraction(file_name)

def get_data_validation(records):
  for record in records:
    ValidationChain().validate(record)

def get_tranformed_data(records):
  tranfsormed = []
  for record in records:
    tranfsormed.append(transform_with_extra_data(record))

  return tranfsormed

if __name__ == "__main__":
    try:
      records = run_extraction("source_data_employee.json","json")
      #print(records)

      get_data_validation(records)

      transformed_data = get_tranformed_data(records)

      DataInserter().insert_record(transformed_data)
    except Exception as e:
      logging.error("Exception Occured: %s", e)

