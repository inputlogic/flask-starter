from faker import Faker
from factory import Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from flask_testing import TestCase

from app import app, db
from app.models.user import User
from app.models.comment import Comment
from app.models.post import Post


fake = Faker()


class BaseTestCase(TestCase):

    def create_app(self):
        self.app = app
        self.db = db
        self.db.create_all()
        return self.app

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    email = Sequence(lambda n: 'user{0}'.format(n))
    password = fake.password()


class PostFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session

    author = SubFactory(UserFactory)
    title = ' '.join(fake.words()).title()
    body = fake.paragraph()


class CommentFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Comment
        sqlalchemy_session = db.session

    author = SubFactory(UserFactory)
    post = SubFactory(PostFactory)
    body = fake.paragraph()
