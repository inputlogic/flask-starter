from datetime import datetime

from . import db


class Comment(db.EmbeddedDocument):
    body = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<Comment: {0}...>'.format(self.body[:25])
