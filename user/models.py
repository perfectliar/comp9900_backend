from django.db import models
from django.contrib.auth.models import User
import uuid


class Myuser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=40, null=False)
    email = models.EmailField(null=False)
    user_identity = models.IntegerField(default=0)

    def __str__(self):
        return self.username


'''
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
