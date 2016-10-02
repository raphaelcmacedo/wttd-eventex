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