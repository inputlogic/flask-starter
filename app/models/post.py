from datetime import datetime

from .. import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    author = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment',
        back_populates='post',
        cascade='all, delete, delete-orphan')

    def __repr__(self):
        return '<Post {0}>'.format(self.title)
