# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_offer_spartan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='kind',
        ),
    ]
