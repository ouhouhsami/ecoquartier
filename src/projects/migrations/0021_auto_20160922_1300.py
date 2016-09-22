# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 13:00
from __future__ import unicode_literals

from django.db import migrations


def update_commune_charte(apps, schema_editor):
    Charte = apps.get_model("projects", "Charte")
    Commune = apps.get_model("projects", "Commune")
    chartes = Charte.objects.exclude(code_insee='')
    signed_charte = [u"Charte seule", u"Engagé", u"Label"]
    for charte in chartes:
        if charte.avancement_dans_la_demarche in signed_charte:
            print charte.avancement_dans_la_demarche
            commune = charte.commune
            commune.charte_ecoquartier = True
            commune.save()


def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_commune_charte_ecoquartier'),
    ]

    operations = [
        migrations.RunPython(update_commune_charte, reverse_func),
    ]