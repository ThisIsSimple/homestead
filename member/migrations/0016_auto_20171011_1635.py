# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_auto_20171011_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
