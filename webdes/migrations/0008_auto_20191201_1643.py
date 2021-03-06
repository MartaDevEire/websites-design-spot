# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-01 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdes', '0007_auto_20191201_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='webdes',
            name='category',
        ),
        migrations.AddField(
            model_name='webdes',
            name='categories',
            field=models.ManyToManyField(related_name='webdes', to='webdes.Category'),
        ),
    ]
