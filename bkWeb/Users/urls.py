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
from django.contrib.auth import views as authViews

app_name = 'Users'
urlpatterns = [
    # path('Login', views.Login.as_view(), name='login'),
    # path('Home', views.Home.as_view(), name='Home'),
    # path('logout', views.Logout, name='Logout'),
    path('register/',views.register.as_view(),name='register'),

    path('login/', authViews.LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),


    path('password_change/', authViews.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/', authViews.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', authViews.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', authViews.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),


]
