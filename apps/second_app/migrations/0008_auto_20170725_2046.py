# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-25 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0007_auto_20170725_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]