# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0016_item_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='city',
        ),
        migrations.RemoveField(
            model_name='item',
            name='city_cookie',
        ),
    ]
