# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_floor_total_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='rated_capacity2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='floor',
            name='rated_capacity3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]