CREATE TABLE unified_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    timestamp TIMESTAMPTZ,
    category VARCHAR(100),
    source_type VARCHAR(50)
);

ALTER TABLE unified_data 
ADD COLUMN extra_data JSONB DEFAULT NULL;

ALTER TABLE unified_data
ADD CONSTRAINT unique_name_category_source_type UNIQUE (name, category, source_type);


CREATE TABLE IF NOT EXISTS public.employee_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
	organization VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100),
    role VARCHAR(100),
    hire_date TIMESTAMPTZ,
    salary NUMERIC,
    source_type VARCHAR(50),           -- 'JSON' or 'CSV'
    timestamp TIMESTAMPTZ DEFAULT now(),
    extra_data JSONB,
    CONSTRAINT unique_employee UNIQUE (name,email, department, source_type)
);