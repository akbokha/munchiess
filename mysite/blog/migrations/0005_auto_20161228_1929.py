# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161228_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='recipeimg'),
        ),
    ]
