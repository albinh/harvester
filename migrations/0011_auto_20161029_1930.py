# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvester', '0010_auto_20161026_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='harvest_state',
            field=models.IntegerField(choices=[(0, 'Ej skördeklar'), (1, 'Skördeklar'), (2, 'Övermogen/slutskördad')], default=0),
        ),
        migrations.AddField(
            model_name='culture',
            name='offset',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cropform',
            name='crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cropforms', to='harvester.Crop'),
        ),
        migrations.AlterField(
            model_name='cropform',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
