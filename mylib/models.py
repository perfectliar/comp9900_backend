from django.db import models
import uuid

class MyLib(models.Model):  # admin and user use the same category, ID would be created by django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lib_user_id = models.ForeignKey('user.Myuser', on_delete=models.CASCADE, default=0)
    lib_goods_id = models.ForeignKey('items.ItemInfo', on_delete=models.CASCADE, default=0)