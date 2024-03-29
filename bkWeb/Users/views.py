from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.utils import timezone
from django.db.models import F
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import views as authViews
from .forms import LoginForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your views here.


# class Login(authViews.LoginView):
#     def __init__(self,request,*args, **kwargs):
#         self.request =request
#         self.form_class = LoginForm
# form_class = LoginForm
# pass

# template_name = 'Users/login.html'
# # success_url = 'Home'
# # 加入以下兩行
# model = User

# def get(self, request, *args, **kwargs):
#     self.request = request
#     if self.request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('myapp:StoreList'))
#     return super().get(self, self.request, *args, **kwargs)

# def post(self, request, *args, **kwargs):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect(reverse('myapp:StoreList'))
#     else:
#         return self.render_to_response(
#             self.get_context_data(errors="帳號密碼有誤"))


# class Home(ListView):
#     model = User
#     template_name = 'Users/home.html'
#     context_object_name = 'Users'

# class Logout(authViews.LogoutView):


# def Logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('Users:Login'))

def toLogin(request):
    return HttpResponseRedirect(reverse('myapp:StoreList'))


class register(CreateView):

    model = get_user_model()
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = 'StoreForm'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = UserCreationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('Users:login'))
        else:
            return self.render_to_response(
            self.get_context_data(form=form))

