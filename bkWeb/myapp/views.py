from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F
from .store_form import StoreForm, FoodForm
from .models import Store,Food

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')


def add_store(request):

    if request.method == 'POST':
        sf = StoreForm(request.POST)
        ff = FoodForm(request.POST)
        if sf.is_valid() and ff.is_valid():
            boss = sf.cleaned_data['boss']
            store_name = sf.cleaned_data['store_name']
            phone = sf.cleaned_data['phone']
            address = sf.cleaned_data['address']
            food_name = ff.cleaned_data['food_name']
            price = ff.cleaned_data['price']

            store=Store.objects.create(boss=boss,store_name=store_name,phone=phone,address=address)
            store.food_set.create(food_name=food_name,price=price)
            boss,store_name,phone,address = ('','','','')
            food_name,price = ('','')
            return HttpResponseRedirect(reverse('myapp:add_store'))
    else:
        sf = StoreForm()
        ff = FoodForm()


    context = {
        'StoreForm': sf,
        'FoodForm': ff
    }
    return render(request, 'myapp/addStore.html', context)
