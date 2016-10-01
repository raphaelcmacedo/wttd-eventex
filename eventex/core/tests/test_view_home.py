from django.test import TestCase
from django.shortcuts import resolve_url


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('home'))

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_subscription_link(self):
        expected = 'href="{}"'.format(resolve_url('subscriptions:new'))
        self.assertContains(self.response,expected)

    def test_speakers(self):
        expectations = ['Grace Hoper', 'http://hbn.link/hopper-pic', 'Alan Turing', 'http://hbn.link/turing-pic']
        with self.subTest():
            for expected in expectations:
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers'.format(resolve_url('home'))
        self.assertContains(self.response, expected)