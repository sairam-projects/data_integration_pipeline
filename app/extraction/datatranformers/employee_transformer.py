import json

TABLE_COLUMNS = [
    "name", "organization", "email", "department", "role",
    "hire_date", "salary", "source_type", "timestamp"
]

def transform_with_extra_data(record: dict):
    structured = {k: record.get(k) for k in TABLE_COLUMNS}
    extra = {k: v for k, v in record.items() if k not in TABLE_COLUMNS}
    structured["extra_data"] = json.dumps(extra) if extra else None
    return structured
