from flask_login import UserMixin

from .. import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))

    posts = db.relationship('Post',
        back_populates='author',
        cascade='all, delete, delete-orphan')

    comments = db.relationship('Comment',
        back_populates='author',
        cascade='all, delete, delete-orphan')

    def __repr__(self):
        return '<User {0}>'.format(self.email)
