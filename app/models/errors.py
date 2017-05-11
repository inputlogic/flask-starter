class ModelError(Exception):
    pass


class NotFoundError(ModelError):
    pass


class ValidationError(ModelError):
    def __init__(self, errors):
        super().__init__('Validation failed')
        self.errors = errors
