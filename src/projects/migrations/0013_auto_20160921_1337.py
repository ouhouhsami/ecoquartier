# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 12:35
from __future__ import unicode_literals
import csv
import os

from django.db import migrations


dir_path = os.path.dirname(os.path.realpath(__file__))

project_fields = ['region', 'ancienne_region', 'n_dept', 'nom_dept', 'code_insee', 'ville', 'nom_ecoquartier', 'population', 'commune_rurale_ou_urbaine', 'situation_territoriale', 'situation_du_quartier', 'type_d_operation', 'nombre_d_habitants_dans_le_quartier', 'nombre_de_logements', 'nombre_de_logements_sociaux', 'superficie_du_quartier_ha', 'epa', 'anru', 'pnr', 'aap_2009', 'aap_2011', 'charte', 'candidat_2013', 'resultats_2013', 'candidat_2014', 'resultats_2014', 'candidat_2015', 'resultats_2015', 'dotation_evaluation', 'commentaires', 'candidat_potentiel_reperage_ad4_2017', 'candidat_2016', 'avancement_dans_la_demarche', 'contact_1_mail', 'contact_1_titre', 'contact_1_prenom_nom', 'contact_2_mail', 'contact_2_titre', 'contact_2_prenom_nom', 'contact_3_mail', 'contact_3_titre', 'contact_3_prenom_nom', 'contact_4_mai', 'contact_4_titre', 'contact_4_prenom_nom', 'contact_5_mail', 'contact_5_titre', 'contact_5_prenom_nom', 'contact_6_mail', 'contact_6_titre', 'contact_6_prenom_nom', 'contact_7_mail', 'contact_7_titre', 'contact_7_prenom_nom']

def import_data(apps, schema_editor):
    Charte = apps.get_model("projects", "Charte")
    path = os.path.join(dir_path, '060810_Tableau_ChartesEQ.csv')
    with open(path) as csvfile:  # , encoding='utf-8' on python 3
        load_reader = csv.reader(csvfile, delimiter=str(u','), quotechar=str(u'"'))
        row = next(load_reader)
        print row
        for row in load_reader:
            charte = Charte.objects.create(**dict(zip(project_fields, row)))


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_charte'),
    ]

    operations = [
    	migrations.RunPython(import_data, reverse_func),
    ]
