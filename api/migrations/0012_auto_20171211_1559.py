# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20171211_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mall',
            name='MCategory',
        ),
        migrations.RemoveField(
            model_name='mall',
            name='MName',
        ),
    ]
