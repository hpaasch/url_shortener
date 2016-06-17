# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 00:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener_app', '0004_auto_20160617_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-click_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='click',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener_app.Bookmark'),
        ),
        migrations.AddField(
            model_name='click',
            name='url_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
