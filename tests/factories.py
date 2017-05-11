from factory import Faker, SubFactory
from factory.mongoengine import MongoEngineFactory

from app.models.user import User
from app.models.comment import Comment
from app.models.post import Post


class UserFactory(MongoEngineFactory):
    class Meta:
        model = User

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    password = Faker('password')


class PostFactory(MongoEngineFactory):
    class Meta:
        model = Post

    author = SubFactory(UserFactory)
    title = Faker('catch_phrase')
    body = Faker('paragraph')


class CommentFactory(MongoEngineFactory):
    class Meta:
        model = Comment

    author = SubFactory(UserFactory)
    post = SubFactory(PostFactory)
    body = Faker('paragraph')
