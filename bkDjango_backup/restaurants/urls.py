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
from .viewsPackage import ListView
from . import views
from django .contrib.auth.decorators import login_required

app_name = 'restaurant'
urlpatterns = [
    path('', views.index, name='hiMom'),
    path('<int:a>/plus/<int:b>', views.add, name='add'),
    path('menu/', views.menu, name='menu'),
    path('restaurant/', login_required(views.show_restaurant), name='restaurant'),
    path('comment/<int:id>', views.comment, name='comment'),
    path('comment2/<int:id>', views.comment2, name='comment2'),
    re_path(r'restaurant/(\w{1,10})',
            views.show_menu, name='show_restaurant'),

    path('cookieSave/', views.cookie_save, name='cookie_save'),
    re_path(r'cookieDelete/(\w{1,10})',
            views.cookie_delete, name='cookie_delete'),

    path('sessionSave/', views.session_save, name='session_save'),
    re_path(r'sessionDelete/(\w{1,10})',
            views.session_delete, name='session_delete'),

    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('backend/', views.backend, name='backend')

    # ListView
    # re_path(r'ListView/(\w{1,10})', ListView.show_menu_ListView.as_view,
    #         name='show_restaurant_Listview'),
    # re_path(r'ListView/(\w{1,10})', ListView.show_menu_ListView,
    #         name='show_restaurant_Listview'),

]
