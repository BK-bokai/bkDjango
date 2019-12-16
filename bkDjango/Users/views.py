from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
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
import redis
import hashlib
import random
from .Lib.mail import sendmail
from django.core.mail import send_mail

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from_email = settings.DEFAULT_FROM_EMAIL


r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# Create your views here.


class register(CreateView):

    model = get_user_model()
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = 'success'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return super().get(self, self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = UserCreationForm(self.request.POST)
        if form.is_valid():

            mailto = request.POST.get('email', None)
            username = request.POST['username']

            # r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            r.set(username, hashlib.sha256(
                str(random.getrandbits(256)).encode('utf-8')).hexdigest(), 300)
            # 將一組亂碼儲存在redis中，並設定5分鐘的期限

            url = request.build_absolute_uri(reverse('Users:confirm', kwargs={
                'username': username,
                'token': r.get(username)
            }
            ))
            sendmail(mailto=mailto, url=url)

            send_mail('Subject here', 'Here is the message.',
                      from_email, [mailto], fail_silently=False)

            user = form.save()
            return HttpResponseRedirect(reverse('Users:login')+"?msg=已註冊完畢，請收取確認信")
        else:
            return self.render_to_response(
                self.get_context_data(form=form))


def confirm(request, username, token):
    user = get_object_or_404(User, username=username)

    if not(token == r.get(username)) or not(r.get(username)):
        raise Http404
    elif token == r.get(username) and r.get(username):
        user = User.objects.filter(username=username)
        user.update(is_active=1)
        r.delete(username)
        return HttpResponseRedirect(reverse('Users:login')+"?msg=感謝您的註冊，您已可進行登入動作")


class members(ListView):
    # template_name = 'myapp/StoreList.html'
    template_name = 'registration/members.html'

    # 與get_queryset配對的變數名稱
    context_object_name = 'members'
    # 定義回傳的資料
    # def get(self, request, *args, **kwargs):
    #     return super().get(self, request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.all()

    # 自定義想要回傳的額外變數
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class addMember(CreateView):
    model = get_user_model()
    template_name = 'registration/addMember.html'
    form_class = UserCreationForm
    success_url = 'success'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = UserCreationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = 1
            user.save()
            return HttpResponseRedirect(reverse('Users:members'))
        else:
            return self.render_to_response(
                self.get_context_data(form=form))


class delMember(DetailView):
    model = get_user_model()

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response_data = {"action": "delete", 'User': pk,
                         'request.is_ajax()': request.is_ajax()}
        return JsonResponse(response_data)


class patchMember(UpdateView):
    model = get_user_model()
    template_name = 'registration/patchMember.html'
    form_class = UserCreationForm
    # queryset = User.objects.all()  # 這很重要
    # # context_object_name = 'members'

    def post(self, request, pk, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.pk = pk
        self.object = self.get_object()
        form = UserCreationForm(
            self.request.POST, instance=self.object)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Users:members'))
            # return self.form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form))


