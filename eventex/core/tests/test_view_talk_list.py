from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.core.models import Talk, Speaker, Course


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

        course = Course.objects.create(
            title='Título do Curso',
            start='09:00',
            description='Descrição do curso',
            slots=20
        )

        speaker = Speaker.objects.create(
            name='Raphael Macedo',
            slug='raphael-macedo',
            photo='http://hbn.link/hopper-pic'
        )

        talk_morning.speakers.add(speaker)
        talk_afternoon.speakers.add(speaker)
        course.speakers.add(speaker)

        self.response = self.client.get(resolve_url('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (3, 'Raphael Macedo'),
            (2, 'Descrição da palestra'),
            (1, 'Título do Curso'),
            (1, '09:00'),
            (1, 'Descrição do curso'),
        ]

        with self.subTest():
            for count, expected in contents:
                with self.subTest():
                    self.assertContains(self.response, expected, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks', 'courses']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)

class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(resolve_url('talk_list'))
        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')

