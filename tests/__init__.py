from flask_testing import TestCase

from app import create_app
from app.models.user import User
from app.models.post import Post


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app()

    def tearDown(self):
        for i in [User, Post]:
            i.drop_collection()
