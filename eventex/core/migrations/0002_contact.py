# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('E', 'Email'), ('P', 'Phone')], max_length=1, verbose_name='Kind')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Speaker')),
            ],
            options={
                'verbose_name': ('Contact',),
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
