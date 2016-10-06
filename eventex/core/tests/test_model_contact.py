from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Contact, Speaker


class ContactModelTest(TestCase):
    def setUp(self):
        #Create speaker
        self.speaker = Speaker.objects.create(
            name='Raphael Macedo',
            slug='raphael-macedo',
            photo='http://hbn.link/hopper-pic'
        )

    def test_email(self):
        self.contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='raphaelcmacedo@hotmail.com'
        )

        self.assertTrue(Contact.objects.exists());

    def test_phone(self):
        self.contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='0000-0000'
        )

        self.assertTrue(Contact.objects.exists());

    def test_choices(self):
        """Contact should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        self.contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='raphaelcmacedo@hotmail.com'
        )
        self.assertEqual('raphaelcmacedo@hotmail.com', str(self.contact))

class ContactManagerTest(TestCase):
    def setUp(self):
        # Speaker
        self.speaker = Speaker.objects.create(
            name='Raphael Macedo',
            slug='raphael-macedo',
            photo='http://hbn.link/hopper-pic'
        )
        # E-mail
        self.speaker.contact_set.create(kind=Contact.EMAIL, value='raphaelcmacedo@hotmail.com')

        # Phone
        self.speaker.contact_set.create(kind=Contact.PHONE, value='0000-0000')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['raphaelcmacedo@hotmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o:o.value)


    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['0000-0000']

        self.assertQuerysetEqual(qs, expected, lambda o:o.value)

