from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from my_portfolio.models import Blogs


class BlogPostTestCase(TestCase):
    def test_no_post(self):
        response = self.client.get(reverse('blog:blogs'))
        self.assertContains(response, 'No found books.')

    # def test_post_list(self):
    #     user = User.objects.create(username='Shake')
    #     user.set_password('1111')
    #     user.save()
    #
    #     user = get_user(self.client)
    #
    #     Blogs.objects.create(title='Title', slug='title', author='user', category='Python', body='Body of post')
    #     blogs = Blogs.objects.all()
    #
    #     response = self.client.get(reverse('blog:blogs'))
    #
    #     for blog in blogs:
    #         self.assertContains(response, blog.title)
