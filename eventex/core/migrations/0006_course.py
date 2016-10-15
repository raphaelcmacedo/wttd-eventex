# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-15 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161015_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Talk')),
                ('slots', models.IntegerField(verbose_name='Slots')),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'verbose_name': ('Course',),
            },
            bases=('core.talk',),
        ),
    ]