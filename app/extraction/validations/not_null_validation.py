import logging

from app.extraction.validations.base_validation import BaseValidation

logging.basicConfig(level=logging.INFO)


class NotNullValidator(BaseValidation):
  REQUIRED_FIELDS = ["name", "organization", "email", "department", "role","hire_date", "salary", "source_type", "timestamp"]

  def do_validate(self, data):
    for field in self.REQUIRED_FIELDS:
      if not data.get(field):
        raise ValueError(f"Validation Error: {field} cannot be null")
    else:
      logging.info("Completed Not Null validation.")
