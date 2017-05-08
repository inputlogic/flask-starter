import re
from datetime import datetime

from cerberus import schema_registry, Validator


registry = schema_registry


class ModelValidator(Validator):
    def _validate_type_objectid(self, value):
        return bool(re.match('[a-f0-9]{24}', value))

    def _validate_type_email(self, value):
        return '@' in value

    def _normalize_default_setter_utcnow(self, _):
        return datetime.utcnow()


def connect(collection=None):
    """
    Lazy load a connection to MongoDB (via pymongo). Optionally return a
    specific collection.

    """
    return None


def register(name, fields):
    """
    Register `fields` to `name` as a schema for `ModelValidator`.

    """
    registry.add(name, fields)
    return ModelValidator(fields)
