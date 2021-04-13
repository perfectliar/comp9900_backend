# Generated by Django 2.2.18 on 2021-04-13 02:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ItemAuthor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_id', models.ForeignKey(default='Unknown name', on_delete=django.db.models.deletion.CASCADE, to='items.Author')),
                ('item_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.ItemInfo')),
            ],
        ),
    ]
