import random

from flask import url_for

from app.tests import BaseTestCase, post_factory


class TestViews(BaseTestCase):
    def test_index_shows_posts(self):
        num_posts = random.randint(2, 10)
        posts = [post_factory(insert=True) for x in range(num_posts)]
        response = self.client.get(url_for('main.index'))
        self.assertTemplateUsed('index.html')

        for post in posts:
            self.assertTrue(post['title'] in str(response.get_data()))
