from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_fields(self):
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected, list(self.form.fields))


class SubscriptionValidation(TestCase):
    def test_cpf_is_digit(self):
        form = self.validated_form(cpf='A2345678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_captilized(self):
        form = self.validated_form(name = 'RAPHAEL MACEDO')
        self.assertEqual('Raphael Macedo', form.cleaned_data['name'])

    def test_email_is_optional(self):
        form = self.validated_form(email = '')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        form = self.validated_form(phone = '')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        form = self.validated_form(email = '', phone = '')
        self.assertListEqual(['__all__'], list(form.errors))

    def validated_form(self, **kwargs):
        valid = dict(name='Raphael Macedo', email='a@a.com', cpf='12345678901', phone='0000-0000')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form

    def assertFormErrorMessage(self, form, field, message):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual(errors_list, [message])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(exception.code, code)