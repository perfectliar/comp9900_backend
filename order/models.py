from django.db import models
from datetime import datetime
import uuid

class MyOrder(models.Model):  # admin and user use the same category, ID would be created by django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_user_id = models.ForeignKey('user.Myuser', on_delete=models.CASCADE, default=0)
    order_status = models.CharField(max_length=30, default='Waiting for payment')
    order_time = models.DateTimeField(default=datetime.now, blank=True)
    total_price = models.IntegerField(default=-1)

class OrderItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey('MyOrder', on_delete=models.CASCADE, default=0)
    order_item_id = models.ForeignKey('items.ItemInfo', on_delete=models.CASCADE, default=0)