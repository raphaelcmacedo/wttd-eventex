from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Raphael Macedo', cpf='00000000000', email='raphaelcmacedo@hotmail.com', phone='(00) 00000-0000'
        )
        self.response = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(self.response.status_code,200)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        values = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        for value in values:
            with self.subTest():
                self.assertContains(self.response, value)


class SubscriptionDetailNotFound(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/0/')

    def test_not_found(self):
        self.assertEqual(self.response.status_code, 404)
