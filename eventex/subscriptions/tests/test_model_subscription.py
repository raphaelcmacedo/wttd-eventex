from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase
from eventex.subscriptions.models  import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Raphael Macedo',
            cpf='12345678901',
            email='raphaelcmacedo@hotmail.com',
            phone='(00)00000-00000'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at,datetime)

    def test_str(self):
        self.assertEqual('Raphael Macedo', str(self.obj))

    def test_paid_default_false(self):
        self.assertEqual(False,self.obj.paid)

    def test_get_absolute_url(self):
        url = resolve_url('subscriptions:detail',self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())