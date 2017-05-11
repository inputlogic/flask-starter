from datetime import datetime

from . import db
from .user import User
from .comment import Comment


class Post(db.Document):
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
    title = db.StringField(max_length=80, required=True)
    body = db.StringField()
    comments = db.EmbeddedDocumentListField(Comment)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<Post: {0}>'.format(self.title)
