# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20161003_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='systeme_projection',
            field=models.CharField(max_length=255),
        ),
    ]
