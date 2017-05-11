from app.models import user as user_model
from app.models.errors import NotFoundError, ValidationError
from app.tests import BaseTestCase, user_factory


class TestUserModel(BaseTestCase):
    def test_emails_must_be_unique(self):
        email = 'duplicate@localhost.local'
        with self.assertRaises(ValidationError) as e:
            user1 = user_model.register(email=email, password='user1')
            user2 = user_model.register(email=email, password='user2')

            self.assertIsNotNone(user1)
            self.assertIsNone(user2)
            self.assertEqual(
                e.errors,
                {'email': ['Email address must be unique']})

    def test_valid_registration_returns_user_id(self):
        profile = user_factory()
        user_id = user_model.register(
            email=profile['email'],
            password=profile['password'])

        self.assertIsNotNone(user_id)

        user = user_model.get_by_id(user_id)
        self.assertTrue(user_model.verify_password(
            profile['password'],
            user['password']))

    def test_valid_login_returns_user(self):
        profile = user_factory()
        user_id = user_model.register(
            email=profile['email'],
            password=profile['password'])

        user = user_model.validate_login(profile['email'], profile['password'])
        self.assertEqual(user_id, user['_id'])

    def test_invalid_login_raises(self):
        with self.assertRaises(NotFoundError):
            user_model.validate_login('foo', 'bar')
