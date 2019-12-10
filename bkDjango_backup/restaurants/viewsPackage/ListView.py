from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F
from ..models import Restaurant, Food, Author, Book
from ..comment_forms import CommentForm
from django.contrib.sessions.models import Session
from django.views.generic import ListView,DetailView

class show_menu_ListView(ListView):
   def __init__(self,request,restaurant):
      self.restaurant = restaurant
      self.request= request

   # model = Restaurant

   template_name = "restaurants/menu.html"
   context_object_name = 'restaurants'
   def get_queryset(self):
        """Return the last five published questions."""
        return get_object_or_404(Restaurant, name=restaurant)


# def show_menu_ListView(request,restaurant):
#    return HttpResponse("hi hi hi")

   