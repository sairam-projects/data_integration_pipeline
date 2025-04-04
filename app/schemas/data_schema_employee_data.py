from pydantic import BaseModel
from typing import Optional, Union, Dict, Any
from datetime import datetime

class EmployeeDataResponse(BaseModel):
    id: int
    name: str
    organization: Optional[str]
    email: str
    department: Optional[str]
    role: Optional[str]
    hire_date: Optional[datetime]
    salary: Optional[float]
    source_type: str
    timestamp: datetime
    extra_data: Optional[Dict[str, Any]]

    class Config:
        orm_mode = True