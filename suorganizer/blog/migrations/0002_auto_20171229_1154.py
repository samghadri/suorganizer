# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'pub_date', 'ordering': ['-pub_date', 'title'], 'verbose_name': 'blog posts'},
        ),
    ]
