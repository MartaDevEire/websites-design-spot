# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-06 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdes', '0012_auto_20191201_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdes',
            name='category',
            field=models.CharField(choices=[('P', 'Professional'), ('E', 'Event'), ('A', 'Abastract'), ('EC', 'Ecommerce'), ('NP', 'Non-Profit')], default='Event', max_length=20),
        ),
    ]