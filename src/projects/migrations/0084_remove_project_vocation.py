# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-20 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0083_auto_20161020_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='vocation',
        ),
    ]