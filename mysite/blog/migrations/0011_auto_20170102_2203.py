# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=-1),
        ),
    ]