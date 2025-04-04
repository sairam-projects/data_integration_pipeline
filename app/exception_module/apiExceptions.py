from fastapi import HTTPException

def data_not_found(detail: str = "Data not found"):
  raise HTTPException(status_code=404, detail=detail)

def invalid_input(detail: str = "Invalid input provided"):
  raise HTTPException(status_code=400, detail=detail)

def unauthorized_access(detail: str = "Unauthorized access"):
  raise HTTPException(status_code=401, detail=detail)

def forbidden_access(detail: str = "Forbidden: You don’t have permission to access this resource"):
  raise HTTPException(status_code=403, detail=detail)

def resource_conflict(detail: str = "Resource conflict: Data already exists"):
  raise HTTPException(status_code=409, detail=detail)

def server_error(detail: str = "Internal Server Error"):
  raise HTTPException(status_code=500, detail=detail)