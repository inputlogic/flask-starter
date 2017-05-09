from datetime import datetime
import importlib

from faker import Faker
from flask_testing import TestCase

import config
import app
from app.models import connect


class BaseTestCase(TestCase):
    def create_app(self):
        return app.create_app()

    def tearDown(self):
        db = connect()
        for name in config.MODELS:
            model = importlib.import_module('app.models.{0}'.format(name))
            db.drop_collection(model.collection)


def user_factory():
    fake = Faker()
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'password': fake.password(),
        'created_at': fake.date_time(),
        'updated_at': fake.date_time()
    }


# class PostFactory(MongoEngineFactory):
#     class Meta:
#         model = Post
#
#     author = SubFactory(UserFactory)
#     title = Faker('catch_phrase')
#     body = Faker('paragraph')
#
#
# class CommentFactory(MongoEngineFactory):
#     class Meta:
#         model = Comment
#
#     author = SubFactory(UserFactory)
#     post = SubFactory(PostFactory)
#     body = Faker('paragraph')
