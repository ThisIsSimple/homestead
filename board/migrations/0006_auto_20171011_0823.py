# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20171010_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
