# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('storage', models.IntegerField()),
                ('pic', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('num', models.IntegerField(default=0)),
                ('clicknum', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.types')),
            ],
        ),
    ]
