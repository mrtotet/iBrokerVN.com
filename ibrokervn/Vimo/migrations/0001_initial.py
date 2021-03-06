# Generated by Django 2.1.4 on 2018-12-23 19:33

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Viewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_list_Vimo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateField(default=datetime.date.today)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('Tenthongtin', models.CharField(max_length=200)),
                ('Anhhuong', models.IntegerField(choices=[(0, 'Xấu'), (1, 'Tốt'), (2, 'Chưa XĐ')], default=2)),
                ('Mucdo', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('CP_anhhuong', models.CharField(max_length=200)),
                ('DangAH', models.IntegerField(choices=[(0, 'Hết AH'), (1, 'Còn AH')], default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WatchList', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
