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
from django .contrib.auth.decorators import login_required
from .views import index
app_name = 'Home'

urlpatterns = [
    path('', index.index.as_view(), name='index'),
    path('backend', login_required(index.bak_Home.as_view(),login_url='/User/login/'), name='back_index'),
    path('checkIndex',login_required(index.checkHome), name='check_index')    
    # path('backend', login_required(index.patchHome,login_url='/User/login/'), name='back_index'),    

    # path('backend', login_required(function=image.bak_image.as_view(), login_url='/User/login/'), name='back_image'),

]
