# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 04:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]