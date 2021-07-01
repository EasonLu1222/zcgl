# Generated by Django 2.2.3 on 2021-07-01 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191123_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroperatelog',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='操作時間'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, max_length=15, verbose_name='部們'),
        ),
    ]
