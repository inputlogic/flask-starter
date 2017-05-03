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
        return '<User: {0}>'.format(self.email)

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_password(password, hash):
        return pbkdf2_sha256.verify(password, hash)

    @staticmethod
    def register(email, password):
        user = User(email=email, password=User.hash_password(password))
        user.save()
        return user

    @staticmethod
    def validate_login(email, password):
        user = User.objects.get(email=email)
        if User.verify_password(password, user.password):
            return user
        raise User.DoesNotExist
