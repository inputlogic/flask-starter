import re
from datetime import datetime

from cerberus import schema_registry, Validator
from pymongo import MongoClient

import config


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
    if not hasattr(connect, 'client'):
        connect.client = MongoClient(
            host=config.MONGODB_HOST,
            port=config.MONGODB_PORT)
        connect.db = connect.client.get_database(config.MONGODB_NAME)

    return connect.db[collection] if collection else connect.db


def register_schema(name, fields):
    """
    Register `fields` to `name` as a schema for `ModelValidator`.

    """
    registry.add(name, fields)
    return ModelValidator(fields)
