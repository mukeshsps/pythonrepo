# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20180112_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
