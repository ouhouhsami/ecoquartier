# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0041_auto_20161004_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='shon_bureauxm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='shon_commercesm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='shon_equipementsm',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
