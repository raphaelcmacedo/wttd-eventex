from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubsciptionsNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('subscriptions:new'))

    def test_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, "subscriptions/subscription_form.html")

    def test_html(self):
        tags = (
            ('<form',1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)


class SubsciptionsNewPostValid(TestCase):
    def setUp(self):
        data = dict(name='Raphael Macedo', cpf='00000000000', email='raphaelcmacedo@hotmail.com',phone='(00) 00000-0000')
        self.response = self.client.post(resolve_url('subscriptions:new'), data)

    def test_post(self):
        self.assertRedirects(self.response,resolve_url('subscriptions:detail', 1))

    def test_send_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubsciptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(resolve_url('subscriptions:new'),{})

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

    def test_not_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

