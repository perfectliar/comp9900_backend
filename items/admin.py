from django.contrib import admin

from .models import ItemInfo, Category, ItemCategory, ItemAuthor, Author

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


class Item_Info(admin.ModelAdmin):
    list_display = ['item_name', 'item_price', 'id']

    class Meta:
        model = ItemInfo


class BookCate(admin.ModelAdmin):
    list_display = ['item_id', 'cate_id', 'id']

    class Meta:
        model = ItemCategory


class Cate(admin.ModelAdmin):
    list_display = ['cag_name', 'id']

    class Meta:
        model = Category


class Item_Author(admin.ModelAdmin):
    list_display = ['item_id', 'author_id', 'id']

    class Meta:
        model = ItemAuthor


class Authors(admin.ModelAdmin):
    list_display = ['author_name', 'id']

    class Meta:
        model = Author


admin.site.register(ItemInfo, Item_Info)
admin.site.register(Category, Cate)
admin.site.register(ItemCategory, BookCate)
admin.site.register(Author, Authors)
admin.site.register(ItemAuthor, Item_Author)
