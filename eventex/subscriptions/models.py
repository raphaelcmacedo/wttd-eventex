from django.db import models

class Subscription (models.Model):
    name = models.CharField('Name', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail')
    phone = models.CharField('Phone number', max_length=20)
    created_at = models.DateTimeField('Created at',auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name