# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20170419_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.FileField(blank=True, upload_to='store_img/%Y/%m/%d')),
                ('url', models.URLField(blank=True)),
                ('city_select_metod', models.CharField(choices=[('NON', ''), ('COO', 'Куки'), ('URD', 'URL(домен 3 уровня)'), ('URF', 'URL(Подпапки)'), ('UAL', 'URL(Все)'), ('FUL', 'Все')], default='NON', max_length=3)),
            ],
        ),
        migrations.RenameField(
            model_name='store',
            old_name='url_domain',
            new_name='city_param',
        ),
        migrations.RemoveField(
            model_name='store',
            name='city_cookie',
        ),
        migrations.RemoveField(
            model_name='store',
            name='city_select_metod',
        ),
        migrations.RemoveField(
            model_name='store',
            name='title',
        ),
        migrations.RemoveField(
            model_name='store',
            name='url_folder',
        ),
        migrations.AddField(
            model_name='city',
            name='short_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='store',
            name='сompetitor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='monitor.Competitors'),
            preserve_default=False,
        ),
    ]
