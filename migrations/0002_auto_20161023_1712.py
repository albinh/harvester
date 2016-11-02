# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvester', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cropform',
            old_name='form',
            new_name='form_name',
        ),
        migrations.AlterField(
            model_name='cropform',
            name='weight_of_one_unit',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
