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
from ..models import Images
from ..form import IMGForm 
import os
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# class bak_image(ListView):
#     template_name = 'Image/image_bak.html'

#     # 與get_queryset配對的變數名稱
#     context_object_name = 'images'

#     def get_queryset(self):
#         return Images.objects.all

 
class bak_image(CreateView):
    template_name = 'Image/image_bak.html'
    model = Images
    form_class = IMGForm
    def get(self, request, *args, **kwargs):
        self.object = None
        images = Images.objects.all()
        return self.render_to_response(
            self.get_context_data(images=images))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        request.FILES['image_file']

        IMG = request.FILES.get('image_file')
        # 改名
        IMGtype = IMG.name.split(".")[-1]
        IMG.name = str(timezone.localtime())+'.'+IMGtype
        # save_path = os.path.join(settings.MEDIA_ROOT, str(IMG))
        # 改名

        # # 改尺寸
        img = Image.open(IMG)
        output_size = (206, 206)
        img.resize(output_size)
        img = img.resize( (200, 200), Image.BILINEAR )
        img.save(IMG)
        return HttpResponse(help(IMG))
        # # 改尺寸
        
        publish = True if int(request.POST['publish']) == 1 else False
        index = False
        create_at = timezone.localtime()

        img = Images(path=IMG,publish=publish,index=index,create_at=create_at)
        img.save()
        return HttpResponse(IMG)

        # if (form.is_valid() and FoodForm.is_valid()):
        #     return self.form_valid(form, FoodForm)
        # else:
        #     return self.form_invalid(form, FoodForm)

# class StoreForm(CreateView):
#     model = Store
#     template_name = 'myapp/StoreForm.html'
#     form_class = InlineStoreForm
#     success_url = 'StoreForm'

#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates blank versions of the form
#         and its inline formsets.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         FoodForm = InlineFoodFormSet()
#         return self.render_to_response(
#             self.get_context_data(sf=form,
#                                   ff=FoodForm))

#     def post(self, request, *args, **kwargs):
#         """
#         Handles POST requests, instantiating a form instance and its inline
#         formsets with the passed POST variables and then checking them for
#         validity.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         FoodForm = InlineFoodFormSet(self.request.POST)
#         if (form.is_valid() and FoodForm.is_valid()):
#             return self.form_valid(form, FoodForm)
#         else:
#             return self.form_invalid(form, FoodForm)


# def bak_image(request):
#     images = Images.objects.all()
#     context = {
#         'images': images,
#     }

#     if request.method == 'POST':
#         return HttpResponse(request.FILES['image_file'])

#     return render(request, 'Image/image_bak.html',context)
