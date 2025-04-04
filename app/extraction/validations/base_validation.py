class BaseValidation:
  def __init__(self, next_validator=None):
    self.next_validator = next_validator

  def validate(self, data):
    self.do_validate(data)
    if self.next_validator:
      self.next_validator.validate(data)

  def do_validate(self, data):
    raise NotImplementedError("Subclasses should implement this method")
