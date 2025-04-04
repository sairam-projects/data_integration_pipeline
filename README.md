
Data Integration Pipeline
Overview

This project is a FastAPI-based data integration pipeline that extracts, transforms, validates, and inserts employee data from JSON and CSV sources into a PostgreSQL database. It follows a modular architecture with clean code separation.

Features
Extract data from JSON and CSV files
Validate data using a validation chain (type checks, null checks, etc.)
Transform data and store extra fields in JSONB format
Load structured and extra data into a PostgreSQL database
FastAPI API to fetch, filter, and aggregate employee records

Project Structure
data_integration_pipeline/
│── app/
│   ├── extraction/       # Extractors and validation logic
│   ├── transformation/   # Data transformation logic
│   ├── api/             # FastAPI routes
│   ├── db/              # Database models & connection
│── tests/                # Unit tests with pytest
│── data/                 # Sample JSON/CSV files
│── requirements.txt      # Required Python dependencies
│── README.md             # Project documentation
│── main.py               # Entry point for FastAPI app

Installation & Setup
Clone the Repository

git clone https://github.com/yourusername/data_integration_pipeline.git
cd data_integration_pipeline
Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

pip install -r requirements.txt

Set Up PostgreSQL Database
Make sure PostgreSQL is installed and update the .env file with the correct credentials.

Run the FastAPI Server

uvicorn app.main:app --reload
Access the API
 http://127.0.0.1:8000/docs for interactive API documentation.

API Endpoints
	• GET /employees → Fetch all employees
	• GET /employees?department=HR → Filter by department
	• POST /employees → Insert new employee data
	• GET /employees/stats → Get aggregated insights

Running Tests

pytest tests/![image](https://github.com/user-attachments/assets/da9aa531-1a3f-412b-accb-94ddad791c03)
