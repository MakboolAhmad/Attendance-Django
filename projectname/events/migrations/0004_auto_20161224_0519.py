# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-24 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20161224_0512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name_plural': 'People'},
        ),
    ]
