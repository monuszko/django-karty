# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karty', '0002_auto_20170328_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'dish', 'verbose_name_plural': 'dishes'},
        ),
        migrations.AlterModelOptions(
            name='menucard',
            options={'verbose_name': 'menu card', 'verbose_name_plural': 'menu cards'},
        ),
    ]