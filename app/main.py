from fastapi import FastAPI
from app.routes import data_routes,employee_data_routes
#from core.config import APP_TITLE

APP_TITLE = "Employee Data Integration API"
app = FastAPI(title=APP_TITLE)

app.include_router(employee_data_routes.router, prefix="/api/v1")