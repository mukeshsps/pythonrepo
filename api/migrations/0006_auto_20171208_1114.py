# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PT_name', models.CharField(help_text='enter Type name', max_length=255)),
                ('PT_status', models.CharField(choices=[('A', 'Avilable'), ('NA', 'Not Avilable'), ('N', 'New stoke'), ('Ol', 'old stoke'), ('O', 'others')], max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='Emp_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('o', 'other')], max_length=1),
        ),
    ]
