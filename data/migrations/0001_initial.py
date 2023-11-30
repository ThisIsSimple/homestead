# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('client_id', models.CharField(max_length=32)),
                ('module_id', models.CharField(max_length=255)),
                ('temp', models.FloatField()),
                ('hum', models.FloatField()),
                ('soil', models.FloatField()),
                ('light', models.FloatField()),
            ],
        ),
    ]