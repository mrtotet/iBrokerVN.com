# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-02 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DexuatGD', '0012_auto_20190402_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update_trade',
            name='DateRecommend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DexuatGD.Recommend'),
        ),
        migrations.AlterField(
            model_name='update_trade',
            name='Stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Update_Trade', to='DexuatGD.Estimate', unique=True),
        ),
    ]