import random

from flask import url_for

from app.tests import BaseTestCase, post_factory


class TestViews(BaseTestCase):
    def test_index_shows_posts(self):
        posts = [post_factory() for x in range(random.randint(2, 10))]
        response = self.client.get(url_for('main.index'))
        self.assertTemplateUsed('index.html')

        for post in posts:
            self.assertTrue(post['title'] in str(response.get_data()))
