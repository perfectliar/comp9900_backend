from django.db import models
import uuid

class GoodsInfo(models.Model):  # admin and user use the same category, ID would be created by django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goods_name = models.CharField(max_length=50)
    goods_price = models.IntegerField(default=0)
    goods_desc = models.TextField()  # description
    # goods_img = models.ImageField(upload_to='goods')

    def __str__(self):
        return self.goods_name

class Category(models.Model):  # admin and user use the same category, ID would be created by django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cag_name = models.CharField(max_length=30)  # name
    cag_name_sample = ['Action and Adventure', 'Classics', 'Comic Book or Graphic Novel', 'Detective and Mystery',
                       'Fantasy']

    def __str__(self):
        return self.cag_name
    # cag_css = models.CharField(max_length=20, null=True)  # front-end css
    # cag_img = models.ImageField(upload_to='cag', null=True)  # images for category

class GoodsCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cate_id = models.ForeignKey('Category', on_delete=models.CASCADE, default=0)
    good_id = models.ForeignKey('GoodsInfo', on_delete=models.CASCADE, default=0)

'''
from django.db import models
from partial_date import PartialDateField, PartialDate
import uuid


class BookInfo(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.FloatField()
    published_time = PartialDateField()
    publisher = models.CharField(max_length=40)
    author = models.CharField(max_length=40)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Book List"

    def __str__(self):
        return self.name


class Category(models.Model):
    cate_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Book_cate(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # cate_id = models.UUIDField(default=uuid.uuid4, editable=False)
    book_id = models.ForeignKey("BookInfo", on_delete=models.CASCADE, related_name='book')
    cate_id = models.ForeignKey("Category", on_delete=models.SET_DEFAULT, related_name='cate')

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Book's Category"

'''