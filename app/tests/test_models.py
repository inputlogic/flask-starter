from app.models import user as user_model
from app.tests import BaseTestCase, user_factory


class TestUserModel(BaseTestCase):
    # def test_emails_must_be_unique(self):
    #     with self.assertRaises(db.NotUniqueError):
    #         for i in range(2):
    #             UserFactory.create(email='duplicate@localhost.local')

    def test_registration(self):
        profile = user_factory()
        user = user_model.register(
            email=profile['email'],
            password=profile['password'])

        self.assertIsNotNone(user)
        self.assertTrue(user_model.verify_password(
            profile['password'],
            user['password']))

    # def test_valid_login_returns_user(self):
    #     password = 'test'
    #     hashed_password = User.hash_password(password)
    #     new_user = UserFactory.create(password=hashed_password)
    #     logged_in_user = User.validate_login(new_user.email, password)
    #     self.assertEqual(new_user.pk, logged_in_user.pk)
    #
    # def test_invalid_login_raises_error(self):
    #     with self.assertRaises(User.DoesNotExist):
    #         User.validate_login('invalid@localhost.local', 'nopesauce')
