from django.db import models
import uuid

class Cart(models.Model):  # admin and user use the same category, ID would be created by django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_user_id = models.ForeignKey('user.Myuser', on_delete=models.CASCADE, default=0)
    cart_goods_id = models.ForeignKey('items.GoodsInfo', on_delete=models.CASCADE, default=0)
