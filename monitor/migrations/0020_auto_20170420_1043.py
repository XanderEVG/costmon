# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0019_auto_20170420_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitors',
            name='short_title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='city',
            name='short_title',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
