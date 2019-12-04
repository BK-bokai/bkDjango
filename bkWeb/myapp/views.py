from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView,CreateView
from django.utils import timezone
from django.db.models import F
from .store_form import StoreForm, FoodForm
from .Formset_form import FoodFormSet
from .inlineformset import InlineStoreForm, InlineFoodFormSet
from .models import Store, Food
from django.shortcuts import render_to_response


# Create your views here.


# def index(request):
#     return render(request, 'myapp/index.html')

class index(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        # 取得字典型態的Context
        context = super().get_context_data(**kwargs)
        # 加入我們額外想要的時間參數
        context["time"] = timezone.now()
        return context


def FormSet(request):
    if request.method == 'POST':
        formset = FoodFormSet(request.POST)
        return HttpResponse(request)
    else:
        formset = FoodFormSet()

    context = {
        'formset': formset
    }
    return render(request, 'myapp/FormSet.html', context)


def inlineformset(request):
    if request.method == 'POST':
        StoreForm = InlineStoreForm(request.POST)
        if StoreForm.is_valid():
            myStore = StoreForm.save()

            FoodForm = InlineFoodFormSet(request.POST, instance=myStore)

            if FoodForm.is_valid():
                FoodForm.save()
            return HttpResponseRedirect(reverse('myapp:InlineForm'))
    else:
        StoreForm = InlineStoreForm()
        FoodForm = InlineFoodFormSet()

    context = {
        'sf': StoreForm,
        'ff': FoodForm
    }
    return render(request, 'myapp/InlineForm.html', context)


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

            store = Store.objects.create(
                boss=boss, store_name=store_name, phone=phone, address=address)
            store.food_set.create(food_name=food_name, price=price)
            boss, store_name, phone, address = ('', '', '', '')
            food_name, price = ('', '')
            return HttpResponseRedirect(reverse('myapp:add_store'))
    else:
        sf = StoreForm()
        ff = FoodForm()

    context = {
        'StoreForm': sf,
        'FoodForm': ff
    }
    return render(request, 'myapp/addStore.html', context)


# class StoreForm(CreateView):
#     template_name = 'myapp/StoreForm.html'
#     form_class = InlineStoreForm

#     def get_success_url(self):
#         return reverse('StoreForm')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context['sf'] = InlineStoreForm(self.request.POST)
#             context['ff'] = InlineFoodFormSet(self.request.POST)
#         else:
#             context['sf'] = InlineStoreForm()
#             context['ff'] = InlineFoodFormSet()
#         return context

#         # Validate forms
#     def form_valid(self, form):
#         context = self.get_context_data()
#         ff = context['ff']
#         if ff.is_valid() and form.is_valid():
#             self.object = form.save() # saves Father and Children
#             return HttpResponseRedirect(reverse('myapp:StoreForm'))
#         else:
#             return self.render_to_response(self.get_context_data(form=form))

#     # 處理沒通過的表單
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))
        
class StoreForm(CreateView):
    model = Store
    template_name = 'myapp/StoreForm.html'
    form_class = InlineStoreForm
    success_url = 'StoreForm'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        FoodForm = InlineFoodFormSet()
        return self.render_to_response(
            self.get_context_data(sf=form,
                                  ff=FoodForm))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        FoodForm = InlineFoodFormSet(self.request.POST)
        if (form.is_valid() and FoodForm.is_valid()):
            return self.form_valid(form, FoodForm)
        else:
            return self.form_invalid(form, FoodForm)

    def form_valid(self, form, FoodForm):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        FoodForm.instance = self.object
        FoodForm.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, FoodForm):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(sf=form,
                                  ff=FoodForm))

class StoreList(ListView):
    template_name = 'myapp/StoreList.html'

    # 與get_queryset配對的變數名稱
    context_object_name = 'StoreList'
    # 定義回傳的資料

    def get_queryset(self):
        return Store.objects.all()

    # 自定義想要回傳的額外變數
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['st1'] = Store.objects.get(id=1)
        return context


class StoreDetail(DetailView):
    template_name = 'myapp/StoreDetail.html'
    context_object_name = 'Store'
    # 會根據傳入的pk值去尋找queryset的資料

    def get_queryset(self):
        return Store.objects.all()
