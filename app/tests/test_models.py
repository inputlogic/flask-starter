from sqlalchemy.exc import IntegrityError

from app.tests import BaseTestCase, UserFactory


class TestModels(BaseTestCase):

    def test_email_unique(self):
        user1 = UserFactory(email='test@localhost.local')
        user2 = UserFactory(email='test@localhost.local')

        with self.assertRaises(IntegrityError):
            self.db.session.add(user1)
            self.db.session.commit()

            self.db.session.add(user2)
            self.db.session.commit()
