from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from sqlalchemy.ext.hybrid import hybrid_property

from .. import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    _password = db.Column(db.String(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = pbkdf2_sha256.hash(plaintext)

    posts = db.relationship(
        'Post',
        back_populates='author',
        cascade='all, delete, delete-orphan')

    comments = db.relationship(
        'Comment',
        back_populates='author',
        cascade='all, delete, delete-orphan')

    def __repr__(self):
        return '<User {0}>'.format(self.email)
