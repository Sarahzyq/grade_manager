# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='precourse',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]