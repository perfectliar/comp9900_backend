# Generated by Django 2.2.18 on 2021-04-10 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210410_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]