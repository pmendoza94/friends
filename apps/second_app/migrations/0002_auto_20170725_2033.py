# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-25 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='first_app.User'),
        ),
    ]
