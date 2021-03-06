# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-01 15:35
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0004_merge_20171030_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Navn')),
                ('text_color', colorfield.fields.ColorField(default='000000', max_length=18, verbose_name='Tekstfarge')),
                ('background_color', colorfield.fields.ColorField(default='ECB61C', max_length=18, verbose_name='Bakgrunnsfarge')),
            ],
            options={
                'verbose_name_plural': 'Kategorier',
                'verbose_name': 'Kategori',
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='categories',
            field=models.ManyToManyField(to='data_models.Category', verbose_name='Kategorier'),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='data_models.Category', verbose_name='Kategorier'),
        ),
        migrations.AddField(
            model_name='show',
            name='categories',
            field=models.ManyToManyField(to='data_models.Category', verbose_name='Kategorier'),
        ),
    ]
