# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
