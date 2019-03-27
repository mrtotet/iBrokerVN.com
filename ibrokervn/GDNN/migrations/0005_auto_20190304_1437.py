# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-04 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDNN', '0004_gdnn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gdnn',
            name='Room_NN_hientai',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='SH_NN',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Total_Room_NN',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Ban',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Ban_KL',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Ban_TT',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_KL_Rong',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Mua',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Mua_KL',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Mua_TT',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_Rong',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Val_TT_Rong',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Ban',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Ban_KL',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Ban_TT',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Mua',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Mua_KL',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Mua_TT',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gdnn',
            name='Vol_Rong',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]