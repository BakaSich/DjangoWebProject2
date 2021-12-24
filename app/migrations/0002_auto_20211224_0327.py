# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-24 00:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 24, 3, 27, 28, 711530), verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 24, 3, 27, 28, 712530), verbose_name='Дата'),
        ),
    ]
