import random

from flask import url_for

from app.tests import BaseTestCase, PostFactory


class TestViews(BaseTestCase):

    def test_index_shows_posts(self):
        posts = PostFactory.create_batch(random.randint(1, 10))
        self.db.session.add_all(posts)
        self.db.session.commit()

        response = self.client.get(url_for('index'))
        self.assertTemplateUsed('index.html')

        for post in posts:
            self.assertTrue(post.title in str(response.get_data()))
