from django.contrib import admin
from .models import Myuser


class PersonAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'user_identity', 'id']

    class Meta:
        model = Myuser


admin.site.register(Myuser, PersonAdmin)