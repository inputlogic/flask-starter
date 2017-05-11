from bson.errors import InvalidId
from bson.objectid import ObjectId

import bcrypt

from . import connect, register_schema
from .errors import NotFoundError, ValidationError


collection = 'users'
db = connect(collection)


def _validate_unique_email(field, value, error):
    if db.find_one({'email': value.lower().strip()}):
        error(field, 'Email address must be unique')


schema = register_schema(collection, {
    'first_name': {
        'type': 'string'
    },
    'last_name': {
        'type': 'string'
    },
    'email': {
        'type': 'email',
        'required': True,
        'validator': _validate_unique_email
    },
    'password': {
        'type': 'string',
        'required': True,
        'minlength': 6
    },
    'created_at': {
        'type': 'datetime',
        'default_setter': 'utcnow'
    },
    'updated_at': {
        'type': 'datetime',
        'default_setter': 'utcnow'
    }
})


def get_by_id(id):
    try:
        user = db.find_one(ObjectId(str(id)))
        if user:
            return user
    except InvalidId:
        pass
    raise NotFoundError


def verify_password(password, hash):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hash.encode('utf-8'))


def hash_password(password):
    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return str(hash, 'utf-8')


def register(email, password):
    if schema.validate({'email': email, 'password': hash_password(password)}):
        return db.insert_one(schema.document).inserted_id
    raise ValidationError(schema.errors)


def validate_login(email, password):
    user = db.find_one({'email': email})
    if user and verify_password(password, user['password']):
        return user
    raise NotFoundError
