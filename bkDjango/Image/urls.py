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
from .views import image

app_name = 'image'
urlpatterns = [
    path('', image.front_image.as_view(), name='image'),
    path('backend', image.bak_image.as_view(), name='back_image'),
    path('DELETE/<int:pk>',image.delete.as_view(), name='img_del'),
    path('PATCH/<int:pk>',image.patch.as_view(), name='img_patch'),

    # path('<int:a>/plus/<int:b>', views.add, name='add'),
    # path('', image.bak_image, name='image'),

]
