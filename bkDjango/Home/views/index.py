from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.db.models import F
from django.shortcuts import render_to_response
from django .contrib.auth.decorators import login_required
from ..models import Index, Student, StudentSkill, Worker, WorkSkill
# Create your views here.


class index(ListView):
    template_name = 'Home/index.html'

    # 與get_queryset配對的變數名稱
    context_object_name = 'index'

    def get_queryset(self):
        return Index.objects.get(id=1)

    # 自定義想要回傳的額外變數
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(id=1)
        context['s_skill'] = StudentSkill.objects.all()
        context['worker'] = Worker.objects.get(id=1)
        context['w_skill'] = WorkSkill.objects.all()
        return context


class bak_Home(ListView):
    template_name = 'Home/index_bak.html'

    # 與get_queryset配對的變數名稱
    context_object_name = 'index'

    def get_queryset(self):
        return Index.objects.get(id=1)

    # 自定義想要回傳的額外變數
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(id=1)
        context['s_skill'] = StudentSkill.objects.all()
        context['worker'] = Worker.objects.get(id=1)
        context['w_skill'] = WorkSkill.objects.all()
        return context


# class patchHome(UpdateView):
#     model = Index
#     template_name = 'Home/index_bak.html'

#     # 與get_queryset配對的變數名稱
#     context_object_name = 'index'

#     def get_queryset(self):
#         return Index.objects.get(id=1)

#     # 自定義想要回傳的額外變數
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['student'] = Student.objects.get(id=1)
#         context['s_skill'] = StudentSkill.objects.all()
#         context['worker'] = Worker.objects.get(id=1)
#         context['w_skill'] = WorkSkill.objects.all()
#         return context

    # queryset = User.objects.all()  # 這很重要
    # # context_object_name = 'members'

    # def post(self, request, pk, *args, **kwargs):
    #     """
    #     Handles POST requests, instantiating a form instance and its inline
    #     formsets with the passed POST variables and then checking them for
    #     validity.
    #     """
    #     self.pk = pk
    #     self.object = self.get_object()
    #     form = UserCreationForm(
    #         self.request.POST, instance=self.object)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('Users:members'))
    #         # return self.form_valid(form)
    #     else:
    #         return self.render_to_response(
    #             self.get_context_data(form=form))


def checkHome(request):
    if request.is_ajax():
        index = Index.objects.get(id=1)
        student = Student.objects.get(id=1)
        worker = Worker.objects.get(id=1)

        index_content_one = request.POST.get('index_content_one',None)
        index_content_two = request.POST.get('index_content_two',None)
        student_content   = request.POST.get('student_content',None)
        worker_content = request.POST.get('worker_content',None)

        if  not(index.content_one  == index_content_one) and\
            not(index.content_two == index_content_two) and\
            not(student.content   == student_content) and\
            not(worker.content    == worker_content):
            return JsonResponse({'change':1})
        else:
            return JsonResponse({'change':0})
    else :
        raise Http404




    context = {
        'index': Index.objects.get(id=1),
        'student': Student.objects.get(id=1),
        's_skill': StudentSkill.objects.all(),
        'worker': Worker.objects.get(id=1),
        'w_skill': WorkSkill.objects.all()
    }

    return render(request, 'Home/index_bak.html', context)
