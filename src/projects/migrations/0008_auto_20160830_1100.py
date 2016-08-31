# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 11:00
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.gis.geos import GEOSGeometry, GeometryCollection


def geo_data(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    projects = Project.objects.all()
    for project in projects:
        if project.coordonnees_geographiques is not '':
            geom = GEOSGeometry(project.coordonnees_geographiques)
            project.coordonnees_geogrpahiques_gis = GeometryCollection(geom)
            project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_coordonnees_geogrpahiques_gis'),
    ]

    operations = [
        migrations.RunPython(geo_data),
    ]
