# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0004_auto_20160618_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
