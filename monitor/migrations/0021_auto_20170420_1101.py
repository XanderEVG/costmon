# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0020_auto_20170420_1043'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Competitors',
            new_name='Competitor',
        ),
    ]
