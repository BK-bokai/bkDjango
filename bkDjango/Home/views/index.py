from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse 
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.db.models import F
from django.shortcuts import render_to_response
from django .contrib.auth.decorators import login_required

# Create your views here.
class index(TemplateView):
    template_name = 'Home/index.html'

    # # 與get_queryset配對的變數名稱
    # context_object_name = 'data'

    # def get_queryset(self):
    #     return Store.objects.all()

    # # 自定義想要回傳的額外變數
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
