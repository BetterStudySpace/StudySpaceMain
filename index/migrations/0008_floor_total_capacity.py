# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20170323_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='total_capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
