# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20171212_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trustadministration',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]
