# Generated by Django 2.2.18 on 2021-04-10 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myorder',
            old_name='lib_user_id',
            new_name='order_user_id',
        ),
        migrations.RenameField(
            model_name='orderitems',
            old_name='order_book_id',
            new_name='order_item_id',
        ),
        migrations.AddField(
            model_name='myorder',
            name='order_time',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='order_status',
            field=models.CharField(max_length=30),
        ),
    ]