"""bkWeb URL Configuration

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
from django.urls import path
from . import views
from django .contrib.auth.decorators import login_required

app_name = 'myapp'
urlpatterns = [
    # path('',views.index, name='index'),
    path('',views.index.as_view(), name='index'),
    path('addStore',views.add_store, name='add_store'),
    path('FormSet',views.FormSet,name='Formset'),
    path('InlineForm',views.inlineformset,name='InlineForm'),

    path('StoreList',login_required(views.StoreList.as_view()),name='StoreList'),
    path('Store/<int:pk>',login_required(views.StoreDetail.as_view()),name='StoreDetail'),
    path('StoreForm',login_required(views.StoreForm.as_view()),name='StoreForm'),
    path('StoreForm/<int:pk>',login_required(views.UpdateStoreForm.as_view()),name='UpdateStoreForm'),
    path('Comment/<int:pk>',login_required(views.Comment.as_view()),name='Comment')

]
