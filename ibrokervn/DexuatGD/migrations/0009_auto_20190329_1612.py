# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-29 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DexuatGD', '0008_nganhdandattt_mau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nganhdandattt',
            name='NgayRecommend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DexuatGD.Recommend'),
        ),
    ]
