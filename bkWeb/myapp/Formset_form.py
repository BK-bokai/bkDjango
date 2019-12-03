from django.forms import formset_factory
from .store_form import FoodForm

FoodFormSet = formset_factory(FoodForm, extra=3,max_num=2)
