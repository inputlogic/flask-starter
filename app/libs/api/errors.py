'''
Application errors
API endpoints should translate other exceptions into one of these exceptions.

'''

import re


class AppError(Exception):
    '''
    Do not instantiate directly, used as base class
    for specific app errors.

    '''
    def __new__(cls, *args, **kwargs):
        if cls is AppError:
            raise TypeError("AppError's can't be instantiated")
        return Exception.__new__(cls, *args, **kwargs)

    @property
    def message(self):
        return self.__str__()


class InvalidData(AppError):
    name = 'INVALID_DATA'
    status_code = 400

    def __init__(self, message, fields):
        self.fields = fields
        super().__init__(message)

    @classmethod
    def from_validation_error(cls, error, message):
        return cls(message, error.to_dict())

    @classmethod
    def from_not_unique_error(cls, error, message):
        # NotUniqueErrors have hiddeous output :(
        # Using regex to figure out which field caused the error
        match = re.search(r'index: ([a-z]+)_[0-9]+', str(error))
        if len(match.groups()) == 0:
            raise error
        field = match.groups(1)[0]
        fields = {field: '{0} is already taken'.format(field)}
        return cls(message, fields)


class NotFound(AppError):
    name = 'NOT_FOUND'
    status_code = 404


class Forbidden(AppError):
    name = 'FORBIDDEN'
    status_code = 403


class NotAuthorized(AppError):
    name = 'NOT_AUTHORIZED'
    status_code = 401


class ServiceUnavailable(AppError):
    name = 'SERVICE_UNAVAILABLE'
    status_code = 503


class UnprocessableEntity(AppError):
    name = 'UNPROCESSABLE_ENTITY'
    status_code = 422
