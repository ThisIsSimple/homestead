# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_auto_20171010_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
