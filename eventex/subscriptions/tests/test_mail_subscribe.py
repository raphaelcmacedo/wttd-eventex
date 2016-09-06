from django.core import mail
from django.test import TestCase


class SubscriptionPostValid(TestCase):
    def setUp(self):
        data = dict(name='Raphael Macedo', cpf='00000000000', email='raphaelcmacedo@hotmail.com',phone='(00) 00000-0000')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        self.assertEqual(self.email.subject, 'Confirmação de inscrição')

    def test_subscription_email_from(self):
        self.assertEqual(self.email.from_email, 'contato@eventex.com.br')

    def test_subscription_email_from(self):
        self.assertEqual(self.email.from_email, 'contato@eventex.com.br')

    def test_subscription_email_body(self):
        contents = ('Raphael Macedo','00000000000', 'raphaelcmacedo@hotmail.com', '(00) 00000-0000' )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
