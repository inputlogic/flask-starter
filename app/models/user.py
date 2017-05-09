from bson.objectid import ObjectId
import bcrypt

from . import connect, register_schema


def _validate_unique_email(field, value, error):
    pass


collection = 'users'
db = connect(collection)
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


def verify_password(password, hash):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hash.encode('utf-8'))


def hash_password(password):
    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return str(hash, 'utf-8')


def register(email, password):
    if schema.validate({'email': email, 'password': hash_password(password)}):
        return db.insert_one(schema.document)
    return None


def validate_login(email, password):
    user = db.find_one({'email': email})
    if user and verify_password(password, user.password):
        return user
    return None


def get_by_id(id):
    return db.find_one(ObjectId(str(id)))
