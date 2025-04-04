from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UnifiedDataResponse(BaseModel):
    id: int
    name: str
    category: str
    source_type: str
    timestamp: datetime

    class Config:
        orm_mode = True
