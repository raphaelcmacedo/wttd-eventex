# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-15 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course_abc_to_mti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseold',
            name='speakers',
        ),
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
