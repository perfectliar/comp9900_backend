from django.contrib import admin

from .models import OrderItems, OrderStatus, MyOrder

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


class Order_Status(admin.ModelAdmin):
    list_display = ['id', 'order_status']

    class Meta:
        model = OrderStatus


class My_Order(admin.ModelAdmin):
    list_display = ['id', 'order_user_id', 'order_status', 'total_price', 'order_time']

    class Meta:
        model = MyOrder


class Order_Items(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'order_item_id']

    class Meta:
        model = OrderItems


# admin.site.register(Book_cate)
admin.site.register(OrderItems, Order_Items)
admin.site.register(MyOrder, My_Order)
admin.site.register(OrderStatus, Order_Status)