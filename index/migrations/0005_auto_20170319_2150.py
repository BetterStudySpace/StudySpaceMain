# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_floor_libname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='name',
            new_name='title',
        ),
    ]
