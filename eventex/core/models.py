from django.db import models

# Create your models here.
from django.shortcuts import resolve_url


class Speaker(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug')
    description = models.TextField('Description', blank=True)
    website = models.URLField('Website', blank=True)
    photo = models.URLField('Photo')

    class Meta:
        verbose_name='Speaker',
        verbose_name_plural='Speakers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('speaker_detail', slug=self.slug)
    
class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Phone')
    )

    speaker = models.ForeignKey('Speaker')
    kind = models.CharField('Kind', max_length=1, choices=KINDS)
    value = models.CharField('Value', max_length=255)

    class Meta:
        verbose_name='Contact',
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.value

