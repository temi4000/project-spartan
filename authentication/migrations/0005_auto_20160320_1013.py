# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20160319_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='profile picture'),
        ),
    ]