from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F


# Create your views here.
class hiMom:
    def index(self):
        return HttpResponse('嗨媽我在這')

    def add(request, a, b):
        context = {
            'a': a,
            'b': b,
            'sum': int(a)+int(b),
            'dif': int(a)+int(b),
            'pro': int(a)*int(b),
            'quo': int(a)/int(b)
        }
        return render(request, 'momapp/math.html', context)
        # return render(request, 'polls/detail.html', {'question': question})
        # return HttpResponse(str(a)+'+'+str(b)+'=' + str(int(a)+int(b)))

    def menu(request):
        food1 = {'name': '番茄炒蛋', 'price': 60,
                 'comment': '好吃', 'is_spicy': False}
        food2 = {'name': '蒜泥白肉', 'price': 100,
                 'comment': '人氣推薦', 'is_spicy': True}
        context = {
            'food1': food1,
            'food2': food2,
            'foods': [food1,food2]
        }
        return render(request, 'momapp/menu.html', context)
