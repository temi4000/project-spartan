# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-29 15:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20160725_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 29, 15, 43, 2, 981617, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]