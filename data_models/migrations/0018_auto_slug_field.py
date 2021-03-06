# Generated by Django 2.0.2 on 2018-10-30 17:58

from django.db import migrations
from django_extensions.db.fields import AutoSlugField


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0017_hide_slug_in_shows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=AutoSlugField(blank=True,
                                editable=False,
                                populate_from=['title']),
        ),
        migrations.AlterField(
            model_name='show',
            name='slug',
            field=AutoSlugField(blank=True,
                                editable=False,
                                populate_from=['name']),
        ),
    ]
