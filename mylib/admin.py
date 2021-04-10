from django.contrib import admin
from .models import MyLib


class LibInfo(admin.ModelAdmin):
    list_display = ['id', 'lib_user_id', 'lib_goods_id']

    class Meta:
        model = MyLib


admin.site.register(MyLib, LibInfo)