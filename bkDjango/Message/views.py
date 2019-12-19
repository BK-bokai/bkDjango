from django.shortcuts import render, get_list_or_404, get_object_or_404
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
from .models import Messages, Replies
from .forms import MsgForm, ReplyForm
from Users.models import User


# Create your views here.


class index(CreateView):
    template_name = 'Message/message.html'
    form_class = MsgForm
    # 與get_queryset配對的變數名稱
    # context_object_name = 'messages'

    # def get_queryset(self):
    #     return Messages.objects.get(id=1)

    # 自定義想要回傳的額外變數
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies = Replies.objects.all()
        messages = Messages.objects.all()
        context['replies'] = replies
        context['messages'] = messages
        context['replyForm'] = ReplyForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = MsgForm(self.request.POST)
        if form.is_valid():
            user = get_object_or_404(User, username=request.user.username)
            # user = User.objects.get(username=request.user.username)
            body = request.POST.get('body', None)
            time = timezone.localtime()
            Messages.objects.create(User=user, body=body, create_at=time)
            return HttpResponseRedirect(reverse('message:message'))
            # return HttpResponse(request.POST.get('body',None))
        else:
            return self.render_to_response(
                self.get_context_data(form=form))


def reply(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.user.username)
        message = get_object_or_404(Messages, pk=pk)
        body = request.POST.get('body', None)
        time = timezone.localtime()
        reply = Replies.objects.create(
            User=user, Message=message, body=body, create_at=time)
        # reply.Message.update(reply_num=int(reply.Message.reply_num)+1)
        reply.Message.reply_num += 1
        reply.Message.save()
        return HttpResponseRedirect(reverse('message:message'))
    else:
        raise Http404


class del_reply(DetailView):
    model = Replies
    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        self.object.Message.reply_num -= 1
        self.object.Message.save()
        self.object.delete()
        response_data = {"action": "delete", 'reply':pk, 'request.is_ajax()':request.is_ajax()}
        return JsonResponse(response_data)

class del_msg(DetailView):
    model = Messages
    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response_data = {"action": "delete", 'message':pk, 'request.is_ajax()':request.is_ajax()}
        return JsonResponse(response_data)

def edit_msg(request,pk):
    if request.method == 'POST' and request.is_ajax() :
        message = get_object_or_404(Messages, pk=pk)
        body = request.POST.get('body', None)
        time = timezone.localtime()
        if message.body == body:
            response_data = {"action": "don't_update", 'message':pk, 'request.is_ajax()':request.is_ajax()}
            return JsonResponse(response_data)
        else:
            message.body = body
            message.update_at=time
            message.save()
            response_data = {"action": "update", 'message':pk, 'request.is_ajax()':request.is_ajax()}
            return JsonResponse(response_data)
    else:
        raise Http404

def edit_reply(request,pk):
    if request.method == 'POST' and request.is_ajax() :
        reply = get_object_or_404(Replies, pk=pk)
        body = request.POST.get('body', None)
        time = timezone.localtime()
        if reply.body == body:
            response_data = {"action": "don't_update", 'reply':pk, 'request.is_ajax()':request.is_ajax()}
            return JsonResponse(response_data)
        else:
            reply.body = body
            reply.update_at=time
            reply.save()
            response_data = {"action": "update", 'reply':pk, 'request.is_ajax()':request.is_ajax()}
            return JsonResponse(response_data)
    else:
        raise Http404
