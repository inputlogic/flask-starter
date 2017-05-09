from bson.objectid import ObjectId

from . import connect, register_schema


collection = 'posts'
db = connect(collection)
schema = register_schema(collection, {
    'author': {
        'type': 'objectid',
        'required': True
    },
    'title': {
        'type': 'string',
        'required': True
    },
    'body': {
        'type': 'string'
    },
    'comments': {
        'type': 'list',
        'schema': {
            'body': {
                'type': 'string',
                'required': True
            },
            'created_at': {
                'type': 'datetime',
                'default_setter': 'utcnow'
            },
            'updated_at': {
                'type': 'datetime',
                'default_setter': 'utcnow'
            }
        }
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


def get_all():
    return db.find_all()


def get_by_id(id):
    return db.find_one(ObjectId(str(id)))
