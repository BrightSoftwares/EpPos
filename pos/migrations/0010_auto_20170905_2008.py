# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-05 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0009_auto_20170905_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='order_lastChange',
            field=models.DateField(auto_now=True),
        ),
    ]