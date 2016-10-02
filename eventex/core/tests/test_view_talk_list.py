from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.core.models import Talk, Speaker


class TalkListGet(TestCase):
    def setUp(self):
        talk_morning = Talk.objects.create(
            title = 'Título da Palestra',
            start = '10:00',
            description = 'Descrição da palestra'
        )

        talk_afternoon = Talk.objects.create(
            title='Título da Palestra',
            start='13:00',
            description='Descrição da palestra'
        )

        speaker = Speaker.objects.create(
            name='Raphael Macedo',
            slug='raphael-macedo',
            photo='http://hbn.link/hopper-pic'
        )

        talk_morning.speakers.add(speaker)
        talk_afternoon.speakers.add(speaker)

        self.response = self.client.get(resolve_url('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)

class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(resolve_url('talk_list'))
        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')

