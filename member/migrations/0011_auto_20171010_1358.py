# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_auto_20171010_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 10, 13, 58, 8, 502349)),
        ),
    ]
