# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 18:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20161003_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='project',
            name='region',
        ),
    ]
