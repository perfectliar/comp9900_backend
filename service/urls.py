"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from items import views as item_views
from cart import views as cart_views
from order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.write_server),
    path('login/', user_views.read_server),


    path('item_list/', item_views.item_list),
    path('item/detail/', item_views.item_detail),
    path('item/add/', item_views.add_item),
    path('item/all_cate/', item_views.all_cate),
    path('item/search/', item_views.search_item),

    path('order/show_all/', order_views.show_all),

    path('cart/show_all/', cart_views.show_all),
    path('cart/add/', cart_views.add),
    path('cart/remove/', cart_views.remove),
    path('cart/clear/', cart_views.clear),
]