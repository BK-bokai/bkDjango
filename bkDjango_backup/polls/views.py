from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
from django.db.models import F


# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     return render(request,'polls/index.html', context)
class IndexView(generic.ListView):
    def __init__(self):
        self.template_name = 'polls/index.html'
        self.context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
           Return the last five published questions (not including those set to be
            published in the future).
        """
        # return Question.objects.order_by('-pub_date')#[:5]
        # return Question.objects.filter(pub_date__lte=timezone.localtime(timezone.now()))\
        #     .order_by('-pub_date')
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selecte_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "請選擇"
        })
    else:
        # selecte_choice.votes +=1
        selecte_choice.votes = F('votes') + 1
        selecte_choice.save()
        # 使用HttpResponseRedirect(reverse())是為了防止用戶按上一頁重新POST造成錯誤
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
