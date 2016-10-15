from django.db import models
from django.shortcuts import resolve_url

from eventex.subscriptions.validators import validate_cpf


class Subscription (models.Model):
    name = models.CharField('Name', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('E-mail', blank=True)
    phone = models.CharField('Phone number', max_length=20, blank=True)
    created_at = models.DateTimeField('Created at',auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('subscriptions:detail',self.pk)