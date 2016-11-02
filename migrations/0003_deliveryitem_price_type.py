# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvester', '0002_auto_20161023_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryitem',
            name='price_type',
            field=models.CharField(choices=[('W', 'efter vikt'), ('U', 'efter enhet')], default='w', max_length=1),
            preserve_default=False,
        ),
    ]
