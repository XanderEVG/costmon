# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_item_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='analogs_items',
            field=models.ManyToManyField(blank=True, to='monitor.AnalogItemsGroup'),
        ),
    ]
