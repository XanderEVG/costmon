# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adder', '0007_importlist_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importlist',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
    ]
