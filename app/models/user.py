from datetime import datetime

import bcrypt
from flask_login import UserMixin

from . import db


class User(UserMixin, db.Document):
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    is_admin = db.BooleanField(default=False)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<User: {0}>'.format(self.email)

    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8'))

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def register(email, password):
        user = User(email=email, password=User.hash_password(password))
        user.save()
        return user

    @staticmethod
    def validate_login(email, password):
        user = User.objects.get(email=email)
        if user.verify_password(password):
            return user
        raise User.DoesNotExist
