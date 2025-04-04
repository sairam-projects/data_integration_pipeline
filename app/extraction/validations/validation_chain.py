from app.extraction.validations.not_null_validation import NotNullValidator
from app.extraction.validations.type_validation import TypeValidation

#app\extraction\validations\type_validation

class ValidationChain:
    def __init__(self):
        # Setup validation chain
        self.chain = NotNullValidator(
            TypeValidation()
        )

    def validate(self, data):
        self.chain.validate(data)
