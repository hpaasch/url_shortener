# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='private',
            field=models.CharField(default='public', max_length=8, verbose_name=('public', 'private')),
        ),
    ]
