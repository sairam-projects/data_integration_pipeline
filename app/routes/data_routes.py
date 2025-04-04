from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.extraction.db_operations.db_sqlalchemy import get_db_session
from app.services.data_services import get_all_records, filter_data, get_aggregated_insights
from app.schemas.data_schema_unified_data import UnifiedDataResponse

router = APIRouter()

@router.get("/records", response_model=list[UnifiedDataResponse])
def fetch_records(db: Session = Depends(get_db_session)):
    return get_all_records(db)

@router.get("/records/filter", response_model=list[UnifiedDataResponse])
def fetch_filtered_records(category: str, db: Session = Depends(get_db_session)):
    return filter_data(db, category)

@router.get("/records/insights")
def fetch_insights(db: Session = Depends(get_db_session)):
    return get_aggregated_insights(db)