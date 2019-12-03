"""bkDjango URL Configuration

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
from django.urls import path, include, re_path
from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.restaurant.index, name='hiMom'),
    path('<int:a>/plus/<int:b>',views.restaurant.add, name = 'add'),
    path('menu/',views.restaurant.menu,name='menu'),
    path('restaurant/',views.restaurant.show_restaurant,name='restaurant'),
    path('comment/<int:id>',views.restaurant.comment,name='comment'),
    path('comment2/<int:id>',views.restaurant.comment2,name='comment2'),
    re_path(r'restaurant/(\w{1,10})',views.restaurant.show_menu, name='show_restaurant'),   
    
]
