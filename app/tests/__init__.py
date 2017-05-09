import importlib
import random

from faker import Faker
from flask_testing import TestCase

import config
import app
from app.models import connect
from app.models import user as user_model
from app.models import post as post_model


fake = Faker()


class BaseTestCase(TestCase):
    def create_app(self):
        return app.create_app()

    def tearDown(self):
        db = connect()
        for name in config.MODELS:
            model = importlib.import_module('app.models.{0}'.format(name))
            db.drop_collection(model.collection)


def user_factory(**kwargs):
    user = {
        'first_name': kwargs.get('first_name', fake.first_name()),
        'last_name': kwargs.get('last_name', fake.last_name()),
        'email': kwargs.get('email', fake.email()),
        'password': kwargs.get('password', fake.password()),
        'created_at': kwargs.get('created_at', fake.date_time()),
        'updated_at': kwargs.get('updated_at', fake.date_time())
    }

    if kwargs.get('insert'):
        user['_id'] = user_model.db.insert_one(user).inserted_id

    return user


def post_factory(**kwargs):
    post = {
        'author': kwargs.get('author', user_factory(insert=True)['_id']),
        'title': kwargs.get('title', fake.sentence()),
        'body': kwargs.get('body', "\n".join(fake.paragraphs())),
        'comments': kwargs.get(
            'comments',
            [comment_factory() for x in range(random.randint(2, 10))]),
        'created_at': kwargs.get('created_at', fake.date_time()),
        'updated_at': kwargs.get('updated_at', fake.date_time())
    }

    if kwargs.get('insert'):
        post['_id'] = post_model.db.insert_one(post).inserted_id

    return post


def comment_factory():
    return {
        'author': user_factory(insert=True)['_id'],
        'body': fake.paragraph(),
        'created_at': fake.date_time(),
        'updated_at': fake.date_time()
    }
