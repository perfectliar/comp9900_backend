# Generated by Django 2.2.18 on 2021-04-07 22:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=50)),
                ('goods_price', models.IntegerField(default=0)),
                ('goods_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cate_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.Category')),
                ('good_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.GoodsInfo')),
            ],
        ),
    ]