# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0018_member_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='code',
            field=models.CharField(default='asdf', max_length=256),
            preserve_default=False,
        ),
    ]
