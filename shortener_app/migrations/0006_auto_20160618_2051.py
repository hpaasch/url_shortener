# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0005_bookmark_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='click',
            name='url_user',
        ),
        migrations.AlterField(
            model_name='click',
            name='click_time',
            field=models.DateTimeField(),
        ),
    ]
