# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contables', '0011_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='final',
            name='es_Actual',
            field=models.NullBooleanField(default=False),
        ),
    ]