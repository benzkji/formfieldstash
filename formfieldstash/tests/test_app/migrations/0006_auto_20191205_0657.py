# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-05 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_auto_20191119_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodelsingle',
            name='bear',
            field=models.DateTimeField(blank=True),
        ),
    ]
