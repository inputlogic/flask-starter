from app import db
from app.tests import BaseTestCase, UserFactory


class TestModels(BaseTestCase):

    def test_email_unique(self):
        with self.assertRaises(db.NotUniqueError):
            for i in range(2):
                UserFactory.create(email='duplicate@localhost.local')
