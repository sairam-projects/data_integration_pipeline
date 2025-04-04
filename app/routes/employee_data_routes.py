from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.extraction.db_operations.db_sqlalchemy import get_db_session
from app.services.employee_data_services import (
    get_all_employee_records,
    filter_by_organization,
    filter_by_organization_and_department,
    filter_by_role,
    get_aggregated_role_salary,
    get_extra_data_by_organization,
    get_employee_count_by_organization
)
from app.schemas.data_schema_employee_data import EmployeeDataResponse

router = APIRouter()

@router.get("/employees", response_model=list[EmployeeDataResponse])
def fetch_all_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    """Fetch all employee records with pagination."""
    return get_all_employee_records(db, skip, limit)

@router.get("/employees/filter/organization", response_model=list[EmployeeDataResponse])
def fetch_by_organization(organization: str, db: Session = Depends(get_db_session)):
    """Filter employees by organization."""
    return filter_by_organization(db, organization)

@router.get("/employees/filter/org-dept", response_model=list[EmployeeDataResponse])
def fetch_by_organization_and_department(organization: str, department: str, db: Session = Depends(get_db_session)):
    """Filter employees by organization and department."""
    return filter_by_organization_and_department(db, organization, department)

@router.get("/employees/filter/role", response_model=list[EmployeeDataResponse])
def fetch_by_role(role: str, db: Session = Depends(get_db_session)):
    """Filter employees by role."""
    return filter_by_role(db, role)

@router.get("/employees/insights")
def fetch_role_salary_aggregation(db: Session = Depends(get_db_session)):
    """Get aggregated data based on roles and average salary."""
    return get_aggregated_role_salary(db)

@router.get("/employees/count")
def fetch_employee_count(db: Session = Depends(get_db_session)):
    return get_employee_count_by_organization(db)

@router.get("/employees/extradata", response_model=list[dict])
def fetch_extra_data(organization: str, db: Session = Depends(get_db_session)):
    """Fetch extra data for employees in a specific organization."""
    return get_extra_data_by_organization(db, organization)
