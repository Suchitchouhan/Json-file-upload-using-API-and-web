"""accountshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from acount.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('api/upload_data',upload_data),
    path('api/get_all_data',get_all_data),
    path('api/create_data',create_data),
    path('api/update_data',update_data),
    path('api/delete_data',delete_data),
    path('api/search_data_by_id',search_data_by_id),
    path('api/search_data_by_time',search_data_by_time),
    path('api/search_data_by_amount',search_data_by_amount),
    path('api/search_data_by_coins_balance',search_data_by_coins_balance),
    
]
