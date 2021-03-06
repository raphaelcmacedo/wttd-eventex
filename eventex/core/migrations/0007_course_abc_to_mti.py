# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-15 12:23
from __future__ import unicode_literals

from django.db import migrations

def copy(Source, Destination):
    for src in Source.objects.all():
        dest = Destination(
            title = src.title,
            start = src.start,
            description = src.description,
            slots = src.slots
        )
        dest.save()
        dest.speakers.set(src.speakers.all())
        src.delete()


def forward_course_abc_to_mti(apps, schema_editor):
    CourseAbc = apps.get_model('core', 'CourseOld')
    CourseMti = apps.get_model('core', 'Course')

    copy(CourseAbc, CourseMti)

def backward_course_abc_to_mti(apps, schema_editor):
    CourseAbc = apps.get_model('core', 'CourseOld')
    CourseMti = apps.get_model('core', 'Course')

    copy(CourseMti, CourseAbc)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti, backward_course_abc_to_mti)
    ]
