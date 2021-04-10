from django.db import models
from datetime import datetime
import uuid

class MyOrder(models.Model):  # admin and user use the same category, ID would be created by django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_user_id = models.ForeignKey('user.Myuser', on_delete=models.CASCADE, default=0)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, default=0)
    order_time = models.DateTimeField(default=datetime.now, blank=True)
    total_price = models.IntegerField(default=-1)

class OrderStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_status = models.CharField(max_length=30)

    def __str__(self):
        return self.order_status

class OrderItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey('MyOrder', on_delete=models.CASCADE, default=0)
    order_item_id = models.ForeignKey('items.GoodsInfo', on_delete=models.CASCADE, default=0)