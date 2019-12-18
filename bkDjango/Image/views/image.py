from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib import messages
from django.template.loader import render_to_string
from django.db.models import F
from django.shortcuts import render_to_response
from django .contrib.auth.decorators import login_required
from django.conf import settings
import time
from ..models import Images
from ..form import IMGForm
import os
from PIL import Image
import os.path
import glob
import re

 
class front_image(ListView):
    template_name = 'Image/image.html'
    model = Images

    # 與get_queryset配對的變數名稱
    context_object_name = 'imgs'

    # 定義回傳的資料
    def get_queryset(self):
        return Images.objects.filter(publish=True)

class bak_image(CreateView):
    template_name = 'Image/image_bak.html'
    model = Images
    form_class = IMGForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.images = Images.objects.all()
        return self.render_to_response(
            self.get_context_data(images=self.images))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        try:
            self.object = None
            IMG = request.FILES.get('image_file')

            # 改名
            IMGtype = IMG.name.split(".")[-1]
            IMG.name = str(time.time())+'.'+IMGtype
            # 改名

            # # 改尺寸並另存新檔
            img = Image.open(IMG)
            width = 426
            height = 420
            new_img = img.resize((width, height), Image.BILINEAR)
            path = os.path.join(settings.MEDIA_ROOT,
                                IMG.name).replace('\\', '/')

            new_img.save(path)
            # # 改尺寸

            publish = True if int(request.POST['publish']) == 1 else False
            index = False
            create_at = timezone.localtime()

            img = Images(path=path, publish=publish,
                         index=index, create_at=create_at)
            img.save()
        except AttributeError as e:
            # messages.success(request,"Your data has been saved!")
            messages.error(request, "圖片有誤!")
            return HttpResponseRedirect(request.path)
        except BaseException as e:
            messages.error(request, "圖片有誤!")
            return HttpResponseRedirect(request.path)

        return HttpResponseRedirect(reverse('image:back_image'))


class delete(DetailView):
    model = Images

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()

        os.remove(self.object.path)
        self.object.delete()
        response_data = {"action": "delete", 'Image':pk, 'request.is_ajax()':request.is_ajax(),'path':self.object.path}
        return JsonResponse(response_data)


class patch(UpdateView):
    model = Images

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        
        publish = request.POST.get('publish')
        img = Images.objects.filter(pk=pk)
        img.update(publish = True if int(publish) == 1 else False)

        response_data = {"action": "patch", 'Image':pk, 'request.is_ajax()':request.is_ajax(), 'publish':publish}
        return JsonResponse(response_data)

class img_home(ListView):
    template_name = 'Home/index_img_bak.html'
    model = Images

    # 與get_queryset配對的變數名稱
    context_object_name = 'imgs'

    # 定義回傳的資料
    def get_queryset(self):
        return Images.objects.all()

def img_home_patch(request):
    old_index_img = Images.objects.filter(index=True)
    old_index_img.update(index=False)
    # return HttpResponse(request.POST.get('index_img',None))
    new_index_img = Images.objects.filter(id=request.POST.get('index_img',None))
    new_index_img.update(index=True)
    return HttpResponseRedirect(reverse('image:img_home'))

def img_home_check(request,pk):
    index_img = Images.objects.get(pk=pk)
    if not(index_img.index):
        response_data = {"change": 1}
        return JsonResponse(response_data)
    else:
        response_data = {"change": 0}
        return JsonResponse(response_data)


