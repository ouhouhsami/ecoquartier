# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0049_auto_20161005_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logements_sociau',
            field=models.TextField(blank=True, null=True),
        ),
    ]