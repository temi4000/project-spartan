# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import phonenumber_field.modelfields
import authentication.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=36, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True)),
                ('profile_image', models.ImageField(height_field='height_field', width_field='width_field', null=True, upload_to=authentication.models.upload_location, blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
    ]
