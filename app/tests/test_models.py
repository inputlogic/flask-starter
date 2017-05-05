from app.models import db
from app.models.user import User
from app.tests import BaseTestCase, UserFactory


class TestUserModel(BaseTestCase):
    def test_emails_must_be_unique(self):
        with self.assertRaises(db.NotUniqueError):
            for i in range(2):
                UserFactory.create(email='duplicate@localhost.local')

    def test_registration(self):
        profile = UserFactory.build()
        user = User.register(email=profile.email, password=profile.password)
        self.assertTrue(user.verify_password(profile.password))
        self.assertIsNotNone(user.id)

    def test_valid_login_returns_user(self):
        password = 'test'
        hashed_password = User.hash_password(password)
        new_user = UserFactory.create(password=hashed_password)
        logged_in_user = User.validate_login(new_user.email, password)
        self.assertEqual(new_user.pk, logged_in_user.pk)

    def test_invalid_login_raises_error(self):
        with self.assertRaises(User.DoesNotExist):
            User.validate_login('invalid@localhost.local', 'nopesauce')
