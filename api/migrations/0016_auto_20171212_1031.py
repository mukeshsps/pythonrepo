# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20171212_1019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Trust',
        ),
        migrations.RemoveField(
            model_name='trustadministration',
            name='user',
        ),
        migrations.DeleteModel(
            name='TrustAdministration',
        ),
    ]
