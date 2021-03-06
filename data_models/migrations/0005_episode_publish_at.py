# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-02 19:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Episode = apps.get_model("data_models", "episode")
    db_alias = schema_editor.connection.alias
    episodes = Episode.objects.using(db_alias).all()
    for episode in episodes:
        episode.publish_at = episode.created_at
        episode.save()


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0004_merge_20171030_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='publish_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
