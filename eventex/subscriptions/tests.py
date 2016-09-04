from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/inscricao/")

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "subscriptions/subscription_form.html")

    def test_html(self):
        self.assertContains(self.response,'<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    def test_has_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'], list(form.fields))


class SubscriptionPostTest(TestCase):
    def setUp(self):
        data = dict(name='Raphael Macedo', cpf='00000000000', email='raphaelcmacedo@hotmail.com',phone='(00) 00000-0000')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, self.response.status_code)

    def test_send_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Confirmação de inscrição')

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        self.assertEqual(email.from_email, 'contato@eventex.com.br')

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        self.assertEqual(email.from_email, 'contato@eventex.com.br')

    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Raphael Macedo', email.body)
        self.assertIn('00000000000', email.body)
        self.assertIn('raphaelcmacedo@hotmail.com', email.body)
        self.assertIn('(00) 00000-0000', email.body)


class SubscriptionInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/',{})

    def test_post(self):
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "subscriptions/subscription_form.html")

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    def test_has_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMessage(TestCase):
    def setUp(self):
        data = dict(name='Raphael Macedo', cpf='00000000000', email='raphaelcmacedo@hotmail.com',phone='(00) 00000-0000')
        self.response = self.client.post('/inscricao/', data, follow=True)

    def test_message(self):
        self.assertContains(self.response, 'Inscrição realizada com sucesso')

