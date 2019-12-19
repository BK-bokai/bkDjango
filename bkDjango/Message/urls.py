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
from django.urls import path, include, re_path, reverse
from django .contrib.auth.decorators import login_required
from django.conf import settings
from . import views


app_name = 'message'
urlpatterns = [
    path('',login_required(views.index.as_view(), login_url='/User/login/'), name = 'message'),
    path('post/reply/<int:pk>',login_required(views.reply, login_url='/User/login/'), name = 'reply'),
    path('Delete/reply/<int:pk>',login_required(views.del_reply.as_view(), login_url='/User/login/'), name = 'del_reply'),
    path('Delete/<int:pk>',login_required(views.del_msg.as_view(), login_url='/User/login/'), name = 'del_msg'),
    path('Patch/<int:pk>',login_required(views.edit_msg, login_url='/User/login/'), name = 'edit_msg'),
    path('Patch/reply/<int:pk>',login_required(views.edit_reply, login_url='/User/login/'), name = 'edit_reply'),
    
    # path('', image.front_image.as_view(), name='image'),
    
    # path('backend', login_required(function=image.bak_image.as_view(), login_url='/User/login/'), name='back_image'),
    # path('DELETE/<int:pk>',login_required(image.delete.as_view()), name='img_del'),
    # path('PATCH/<int:pk>',login_required(image.patch.as_view()), name='img_patch'),

    # path('Index_img',login_required(function=image.img_home.as_view(), login_url='/User/login/'), name='img_home'),
    # path('Check_index_img/<int:pk>',login_required(function=image.img_home_check, login_url='/User/login/'), name='check_img_home'),
    # path('Index/Patch',login_required(function=image.img_home_patch, login_url='/User/login/'), name='patch_img_home'),
    
]
