# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-04 02:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GDNN', '0002_viewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gdnn',
            name='author',
        ),
        migrations.DeleteModel(
            name='GDNN',
        ),
    ]
