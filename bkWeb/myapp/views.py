from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.db.models import F
from .store_form import StoreForm, FoodForm
from .Formset_form import FoodFormSet
from .inlineformset import InlineStoreForm, InlineFoodFormSet
from .models import Store, Food, Comment
from django.shortcuts import render_to_response
from django .contrib.auth.decorators import login_required
from .commentForm import CommentForm


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


class UpdateStoreForm(UpdateView):
    model = Store
    template_name = 'myapp/UpdateStoreForm.html'
    form_class = InlineStoreForm
    queryset = Store.objects.all()  # 這很重要

    def get(self, request, pk, *args, **kwargs):
        self.pk = pk
        self.object = self.get_object()

        form = InlineStoreForm(instance=self.object)
        FoodForm = InlineFoodFormSet(instance=self.object)

        return self.render_to_response(
            self.get_context_data(sf=form,
                                  ff=FoodForm))

    def post(self, request, pk, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.pk = pk
        self.object = self.get_object()
        form = InlineStoreForm(
            self.request.POST, instance=self.object)
        FoodForm = InlineFoodFormSet(
            self.request.POST, instance=self.object)

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
        form.save()
        FoodForm.save()
        return HttpResponseRedirect(reverse('myapp:UpdateStoreForm', args=[self.pk]))

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
    # def get(self, request, *args, **kwargs):
    #     return super().get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Store.objects.all()

    # 自定義想要回傳的額外變數
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StoreDetail(DetailView):
    template_name = 'myapp/StoreDetail.html'
    context_object_name = 'Store'
    # 會根據傳入的pk值去尋找queryset的資料

    def get_queryset(self):
        return Store.objects.all()


class Comment(CreateView):
    model = Comment
    template_name = 'myapp/Comment.html'
    form_class = CommentForm
    success_url = 'StoreForm'

    def get(self, request, pk, *args, **kwargs):
        self.pk = pk
        self.object = None
        return super().get(self, request, pk, *args, **kwargs)
    # 自定義想要回傳的額外變數

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store = Store.objects.get(pk=self.pk)
        context['store'] = store
        return context

    def post(self, request, pk, *args, **kwargs):
        self.pk=pk
        self.object = None
        store = Store.objects.get(pk=self.pk)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            visitor = request.POST['visitor']
            email   = request.POST['email']
            content = request.POST['content']
            publish_date = timezone.localtime()
            store.comment_set.create(visitor=visitor,email=email,content=content,publish_date=publish_date)
            return HttpResponseRedirect(reverse('myapp:Comment', args=[self.pk]))
        else:
            return self.render_to_response(
                self.get_context_data(form=form,
                                      store=store))

    # def form_valid(self, form, FoodForm):
    #     """
    #     Called if all forms are valid. Creates a Recipe instance along with
    #     associated Ingredients and Instructions and then redirects to a
    #     success page.
    #     """
    #     self.object = form.save()
    #     FoodForm.instance = self.object
    #     FoodForm.save()
    #     return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form, FoodForm):
    #     """
    #     Called if a form is invalid. Re-renders the context data with the
    #     data-filled forms and errors.
    #     """
    #     return self.render_to_response(
    #         self.get_context_data(sf=form,
    #                               ff=FoodForm))
