from . import connect, register


collection = 'posts'
db = connect(collection)
schema = register(collection, {
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
