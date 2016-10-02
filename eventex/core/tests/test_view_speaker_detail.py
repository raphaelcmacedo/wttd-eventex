from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.core.models import Speaker


class SpeakerDetailGet(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            description='Programadora e almirante \
                                     Inventora do compilador, criadora da linguagem \
                                     de programação flow-matic serviu de base para a linguagem \
                                     COBOL permitindo a popularização das aplicações comerciais',
            website='http://hbn.link.hopper-site',
            photo='http://hbn.link.hopper-pic'
        )

        self.response = self.client.get(resolve_url('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link.hopper-pic',
            'http://hbn.link.hopper-site'
        ]

        with self.subTest():
            for content in contents:
                self.assertContains(self.response, content)

    def test_context(self):
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)

    def test_not_found(self):
        response = self.client.get(resolve_url('speaker_detail',slug='not-found'))
        self.assertEqual(404, response.status_code)