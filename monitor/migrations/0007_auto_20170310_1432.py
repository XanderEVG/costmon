# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20170310_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='city_select_metod',
            field=models.CharField(blank=True, choices=[('NON', ''), ('COO', 'Куки'), ('URB', 'URL(домен 3 уровня)'), ('URA', 'URL(Подпапки)'), ('UAL', 'URL(Все)'), ('FUL', 'Все')], default='NON', max_length=3),
        ),
    ]
