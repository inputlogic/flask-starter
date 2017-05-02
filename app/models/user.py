from datetime import datetime

from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256

from .. import db


class User(UserMixin, db.Document):
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<User: {2}>'.format(self.email)
