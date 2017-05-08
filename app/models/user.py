import bcrypt

from . import connect, register


def _validate_unique_email(field, value, error):
    pass


collection = 'users'
db = connect(collection)
schema = register(collection, {
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


def verify_password(self, password, hash):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hash.encode('utf-8'))


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def register(email, password):
    return db.insert_one(email=email, password=hash_password(password))


def validate_login(email, password):
    user = db.find_one({'email': email})
    if user and verify_password(password, user.password):
        return user
    return None
