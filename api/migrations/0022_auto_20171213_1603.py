# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20171213_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(help_text='Enter Customer name', max_length=255)),
                ('customer_address', models.TextField()),
                ('Phone_number', models.CharField(help_text='enter phone number', max_length=255)),
                ('Order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='UserProfile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
