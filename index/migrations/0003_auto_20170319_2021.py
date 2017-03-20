# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_floor_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='floor',
            name='current_capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='floor',
            name='floor_number',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='floor',
            name='rated_capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
