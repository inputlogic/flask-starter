from tests import BaseTestCase
from tests.factories import UserFactory
from app.models.user import User


class TestAdminViews(BaseTestCase):
    def setUp(self):
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.password = 'muchsecurepassword'
        self.hashed_password = User.hash_password(self.password)

        self.admin = UserFactory.create(
                email='admin@localhost.local',
                password=self.hashed_password,
                is_admin=True)

    def test_admin_sucessful_login(self):
        login = self.client.post('/admin/login',
                data=dict(email=self.admin.email, password=self.password))
        self.assertTrue('/admin/users' in login.location)

    def test_admin_create_user(self):
        c = self.app.test_client()
        login = c.post('/admin/login',
                data=dict(email=self.admin.email, password=self.password))
        create_user = c.post(
            '/admin/users/create',
            data=dict(
                first_name='first',
                last_name='last',
                email='user@localhost.local',
                password=self.password
        ), follow_redirects=True)

        self.assertMessageFlashed('User created', 'success')
        with self.assertEqual(get_user.email, 'user@localhost.local'):
            get_user = User.objects.get(email='user@localhost.local')
