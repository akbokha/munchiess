# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161228_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pizza',
            field=models.IntegerField(default=0),
        ),
    ]
