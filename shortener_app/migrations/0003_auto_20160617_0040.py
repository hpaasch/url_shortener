# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0002_click_private'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Click',
            new_name='BookmarkList',
        ),
    ]
