from django.shortcuts import render, get_object_or_404
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
import redis
import hashlib
import random
from .Lib.mail import sendmail

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# Create your views here.
class register(CreateView):

    model = get_user_model()
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = 'success'

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

    


