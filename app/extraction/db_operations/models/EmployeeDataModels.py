from sqlalchemy import Column, Integer, String, Numeric, DateTime, JSON
from sqlalchemy.sql import func
from app.extraction.db_operations.db_sqlalchemy import Base

class EmployeeData(Base):
    __tablename__ = "employee_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    organization = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False)
    department = Column(String(100), nullable=True)
    role = Column(String(100), nullable=True)
    hire_date = Column(DateTime(timezone=True), nullable=True)
    salary = Column(Numeric, nullable=True)
    source_type = Column(String(50), nullable=False)  # JSON or CSV
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    extra_data = Column(JSON, nullable=True)

    __table_args__ = (
        # Matches your unique constraint in the table
        {'sqlite_autoincrement': True},
    )