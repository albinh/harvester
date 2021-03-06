# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=10)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CropForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(max_length=40)),
                ('weight_of_one_unit', models.DecimalField(decimal_places=2, max_digits=2)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('variety', models.CharField(max_length=100)),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Bed')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.DecimalField(decimal_places=1, max_digits=5)),
                ('price_unit', models.CharField(max_length=40, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('discount', models.FloatField(default=0.0)),
                ('order_comment', models.CharField(blank=True, default='', max_length=100)),
                ('delivery_comment', models.CharField(blank=True, default='', max_length=100)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Crop')),
                ('crop_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.CropForm')),
            ],
        ),
        migrations.CreateModel(
            name='DeliverySingle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_date', models.DateField(default=datetime.datetime.now)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='HarvestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=datetime.datetime.now)),
                ('harvested_length', models.DecimalField(decimal_places=1, max_digits=4)),
                ('comment', models.CharField(blank=True, max_length=500)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5)),
                ('count', models.DecimalField(decimal_places=0, max_digits=5)),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Culture')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.DeliverySingle')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.PriceList'),
        ),
        migrations.AddField(
            model_name='deliverysingle',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.PriceList'),
        ),
        migrations.AddField(
            model_name='deliveryitem',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.DeliverySingle'),
        ),
        migrations.AddField(
            model_name='customer',
            name='default_pricelist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvester.PriceList'),
        ),
    ]
