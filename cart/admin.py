from django.contrib import admin
from .models import Cart


class CartInfo(admin.ModelAdmin):
    list_display = ['cart_user_id', 'cart_goods_id', 'id']

    class Meta:
        model = Cart


admin.site.register(Cart, CartInfo)