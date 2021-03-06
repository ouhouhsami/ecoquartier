# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0087_auto_20161102_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('engagement', models.IntegerField()),
                ('state', models.CharField(choices=[('01', 'A faire'), ('02', 'En cours'), ('03', 'Fait')], default='01', max_length=2)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
