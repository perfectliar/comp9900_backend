from django.contrib import admin

from .models import GoodsInfo, Category, GoodsCategory

'''
from django.db import models
from tinymce.widgets import TinyMCE

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Name", {"fields": ['name', 'price', 'author', 'description']}),
        ("Publish", {"fields": ['published_time', 'publisher']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
'''


class BookInfo(admin.ModelAdmin):
    list_display = ['id', 'goods_name', 'goods_price']

    class Meta:
        model = GoodsInfo


class BookCate(admin.ModelAdmin):
    list_display = ['id', 'cate_id', 'good_id']

    class Meta:
        model = GoodsCategory


class Cate(admin.ModelAdmin):
    list_display = ['id', 'cag_name']

    class Meta:
        model = Category


# admin.site.register(Book_cate)
admin.site.register(GoodsInfo, BookInfo)
admin.site.register(Category, Cate)
admin.site.register(GoodsCategory, BookCate)

# admin.site.register(Book, BookAdmin)
