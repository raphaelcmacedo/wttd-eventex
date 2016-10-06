from django.db import models
from django.shortcuts import resolve_url

from eventex.core.managers import KindQuerySet, PeriodManager


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

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name='Contact',
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField('Title', max_length=200)
    start = models.TimeField('Start', blank=True, null=True)
    description = models.TextField('Description', blank=True)

    speakers = models.ManyToManyField('Speaker', blank=True)

    objects = PeriodManager()

    class Meta:
        verbose_name='Contact',
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.title

