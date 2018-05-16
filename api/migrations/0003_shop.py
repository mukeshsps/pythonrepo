# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_mall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SName', models.CharField(help_text='Enter shop Name', max_length=255)),
                ('SCategory', models.CharField(help_text='Enter shop Category', max_length=255)),
                ('Shop_number', models.CharField(help_text='Enter shop number', max_length=255)),
                ('S_status', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('Shop_type', models.ManyToManyField(blank=True, to='api.ShopType', verbose_name='Product type')),
            ],
        ),
    ]