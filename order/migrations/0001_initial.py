# Generated by Django 2.2.18 on 2021-04-11 18:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '__first__'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('total_price', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.MyOrder')),
                ('order_item_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.ItemInfo')),
            ],
        ),
        migrations.AddField(
            model_name='myorder',
            name='order_status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.OrderStatus'),
        ),
        migrations.AddField(
            model_name='myorder',
            name='order_user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.Myuser'),
        ),
    ]
