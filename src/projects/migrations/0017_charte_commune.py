# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_remove_project_code_insee'),
    ]

    operations = [
        migrations.AddField(
            model_name='charte',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Commune'),
        ),
    ]
