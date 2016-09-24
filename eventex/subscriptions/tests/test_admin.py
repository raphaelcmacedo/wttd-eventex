from unittest.mock import Mock

from django.test import TestCase

from eventex.subscriptions.admin import admin
from eventex.subscriptions.admin import SubscriptionModelAdmin
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        Subscription.objects.create(name='Raphael Macedo', cpf='12345678901', email='a@a.com', phone='000000-00000')

    def test_has_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        mock = self.call_action()
        mock.assert_called_once_with(None, '1 subscription was marked as paid')

    def call_action(self):
        query_set = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, query_set)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock