# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0012_auto_20170310_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='synonyms',
        ),
        migrations.AddField(
            model_name='analogitemsgroup',
            name='synonyms',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
