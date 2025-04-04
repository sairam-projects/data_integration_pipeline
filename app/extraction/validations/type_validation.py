import datetime
import logging

from app.extraction.validations.base_validation import BaseValidation

logging.basicConfig(level=logging.INFO)


import datetime
import logging
from .base_validation import BaseValidation

class TypeValidation(BaseValidation):
  def do_validate(self, data):
    try:

      if not isinstance(data.get("name"), str):
        raise TypeError("Validation Error: name must be a string")

      if not isinstance(data.get("organization"), str):
        raise TypeError("Validation Error: organization must be a string")

      if not isinstance(data.get("email"), str):
        raise TypeError("Validation Error: email must be a string")

      if not isinstance(data.get("department"), str):
        raise TypeError("Validation Error: department must be a string")

      if not isinstance(data.get("role"), str):
        raise TypeError("Validation Error: role must be a string")

      if not isinstance(data.get("source_type"), str):
        raise TypeError("Validation Error: source_type must be a string")

      if data.get("hire_date") and not isinstance(data.get("hire_date"), (str, datetime.datetime)):
        raise TypeError("Validation Error: hire_date must be a string or datetime")

      if data.get("salary") is not None and not isinstance(data.get("salary"), (int, float)):
        raise TypeError("Validation Error: salary must be a number or numeric string")

      if data.get("timestamp") and not isinstance(data.get("timestamp"), (str, datetime.datetime)):
        raise TypeError("Validation Error: timestamp must be a string or datetime")

    except Exception as e:
      logging.error("Type validation error: %s", e)
    else:
      logging.info("Completed Type validation.")