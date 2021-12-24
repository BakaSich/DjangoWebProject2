# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-24 10:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211224_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 24, 13, 58, 38, 472826), verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 24, 13, 58, 38, 473832), verbose_name='Дата'),
        ),
    ]