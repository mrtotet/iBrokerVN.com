# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-07 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DexuatGD', '0018_auto_20190408_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='Recommends', to='DexuatGD.Recommend_Category'),
        ),
    ]
