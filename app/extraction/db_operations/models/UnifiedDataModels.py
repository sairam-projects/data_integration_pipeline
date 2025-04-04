from sqlalchemy import Column, Integer, String, Float, DateTime
from app.extraction.db_operations.db_sqlalchemy import Base

class UnifiedData(Base):
    __tablename__ = "unified_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    category = Column(String, nullable=True)
    source_type = Column(String, nullable=False)
