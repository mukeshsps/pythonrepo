# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171208_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(help_text='Enter Product Name', max_length=255)),
                ('P_image', models.ImageField(upload_to='media/document/product/%Y/%m/%d/')),
                ('p_Cost', models.CharField(help_text='Enter Product Cost', max_length=255)),
                ('PT_status', models.CharField(choices=[('A', 'Avilable'), ('NA', 'Not Avilable'), ('N', 'New stoke'), ('Ol', 'old stoke'), ('O', 'others')], max_length=1)),
                ('P_features', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('P_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ProductType')),
            ],
        ),
    ]
