from sqlalchemy.orm import Session
from app.extraction.db_operations.models.UnifiedDataModels import UnifiedData
#from app.schemas.data_schema_unified_data import UnifiedDataCreate
from sqlalchemy.orm import Session
from app.exception_module.apiExceptions import data_not_found, resource_conflict, invalid_input

def get_all_records(db: Session):

  print("coming here")

  records = db.query(UnifiedData).all()

  print("coming here")

  if not records:
    data_not_found("No records found in the database")
  return records

def filter_data(db: Session, category: str):
  if not category:
    invalid_input("Category is required for filtering")

  records = db.query(UnifiedData).filter(UnifiedData.category == category).all()
  if not records:
    data_not_found(f"No records found for category: {category}")

  return records

def get_aggregated_insights(db: Session):
  count = db.query(UnifiedData).count()
  if count == 0:
    data_not_found("No data available for aggregation")

  unique_source_types = db.query(UnifiedData.source_type).distinct().count()
  return {"total_records": count, "unique_source_types": unique_source_types}
