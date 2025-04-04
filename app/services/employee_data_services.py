from sqlalchemy.orm import Session
from sqlalchemy import func
from app.extraction.db_operations.models.EmployeeDataModels import EmployeeData
from app.exception_module.apiExceptions import data_not_found, invalid_input
from typing import List, Optional

def get_all_employee_records(db: Session, skip: int = 0, limit: int = 10):
    """Fetch all employee records with pagination."""
    records = db.query(EmployeeData).offset(skip).limit(limit).all()
    if not records:
        data_not_found("No records found in the database")
    return records

def filter_by_organization(db: Session, organization: str):
    """Filter employee records by organization."""
    if not organization:
        invalid_input("Organization is required for filtering")
    
    records = db.query(EmployeeData).filter(EmployeeData.organization == organization).all()
    if not records:
        data_not_found(f"No records found for organization: {organization}")
    
    return records

def filter_by_organization_and_department(db: Session, organization: str, department: str):
    """Filter employee records by organization and department."""
    if not organization or not department:
        invalid_input("Both organization and department are required for filtering")

    records = db.query(EmployeeData).filter(
        EmployeeData.organization == organization,
        EmployeeData.department == department
    ).all()
    
    if not records:
        data_not_found(f"No records found for organization '{organization}' and department '{department}'")
    
    return records

def filter_by_role(db: Session, role: str):
    """Filter employee records by role."""
    if not role:
        invalid_input("Role is required for filtering")

    records = db.query(EmployeeData).filter(EmployeeData.role == role).all()
    if not records:
        data_not_found(f"No records found for role: {role}")
    
    return records

def get_aggregated_role_salary(db: Session):
    """Get aggregated data for roles and average salary."""
    aggregated_data = db.query(
        EmployeeData.role,
        func.round(func.avg(EmployeeData.salary), 2).label("average_salary")
    ).group_by(EmployeeData.role).all()

    if not aggregated_data:
        data_not_found("No data available for aggregation")
    
    return [{"role": role, "average_salary": avg_salary} for role, avg_salary in aggregated_data]

def get_employee_count_by_organization(db: Session):
    """Get count of employees grouped by organization."""
    employee_count = db.query(
        EmployeeData.organization,
        func.count(EmployeeData.id).label("employee_count")
    ).group_by(EmployeeData.organization).all()

    if not employee_count:
        data_not_found("No employee data available")

    return [{"organization": org, "employee_count": count} for org, count in employee_count]

def get_extra_data_by_organization(db: Session, organization: str):
    """Fetch extra data for employees in a specific organization."""
    if not organization:
        invalid_input("Organization is required for fetching extra data")

    records = db.query(EmployeeData.extra_data).filter(EmployeeData.organization == organization).all()
    
    if not records:
        data_not_found(f"No extra data found for organization: {organization}")
    
    return [record.extra_data for record in records if record.extra_data]
