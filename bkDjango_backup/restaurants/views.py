from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F
from .models import Restaurant, Food, Author, Book
from .comment_forms import CommentForm
from django.contrib.sessions.models import Session
from django.contrib import auth

# Create your views here.


def index(request):
    return HttpResponse('嗨媽我在這')


def add(request, a, b):
    context = {
        'a': a,
        'b': b,
        'sum': int(a)+int(b),
        'dif': int(a)+int(b),
        'pro': int(a)*int(b),
        'quo': int(a)/int(b)
    }
    return render(request, 'momapp/math.html', context)
    # return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse(str(a)+'+'+str(b)+'=' + str(int(a)+int(b)))


def menu(request):
    food1 = {'name': '番茄炒蛋', 'price': 60,
             'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100,
             'comment': '人氣推薦', 'is_spicy': True}
    context = {
        'food1': food1,
        'food2': food2,
        'foods': [food1, food2]
    }
    return render(request, 'momapp/menu.html', context)


def show_menu(request, restaurant):
    r = get_object_or_404(Restaurant, name=restaurant)
    # return HttpResponse(r)
    context = {
        'restaurant': r
    }
    return render(request, 'restaurants/menu.html', context)


def show_restaurant(request):
    r = Restaurant.objects.all()
    context = {
        'restaurants': r
    }
    return render(request, 'restaurants/index.html', context)


def comment(request, id):
    r = get_object_or_404(Restaurant, id=id)

    if request.method == "POST":
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        errors = []
        if any(not request.POST[k] for k in request.POST):
            errors.append('* 有空白欄位，請不要留空')

        if (not ('@' in request.POST['email'])) or (not ('.' in request.POST['email'])):
            errors.append('* 請輸入正確Email格式')

        if not(errors):
            r.comment_set.create(
                visitor=visitor, email=email, content=content, publish_date=date_time)
            visitor, email, content = ['', '', '']
            # 使用HttpResponseRedirect(reverse())是為了防止用戶按上一頁重新POST造成錯誤
            return HttpResponseRedirect(reverse('restaurant:comment', args=(r.id,)))
        else:
            context = {
                'visitor': visitor,
                'content': content,
                'email': email,
                'errors': errors,
                'restaurant': r
            }
            return render(request, 'restaurants/comment.html', context)
    else:
        context = {
            'restaurant': r
        }
        return render(request, 'restaurants/comment.html', context)


def comment2(request, id):
    # 判斷是不是post過來的，如果是就進行判斷如果is_valid為true就創建一則評論，False則將這份form回傳回去
    # 若不是post過來得就會傳一份空白表單過去
    r = get_object_or_404(Restaurant, id=id)
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = f.cleaned_data['visitor']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = timezone.localtime(timezone.now())
            r.comment_set.create(
                visitor=visitor, email=email, content=content, publish_date=date_time)
            visitor, email, content = ['', '', '']
            # 使用HttpResponseRedirect(reverse())是為了防止用戶按上一頁重新POST造成錯誤
            return HttpResponseRedirect(reverse('restaurant:comment2', args=(r.id,)))
    else:
        f = CommentForm(initial={'content': '我沒意見'})

    context = {
        'restaurant': r,
        'f': f
    }
    return render(request, 'restaurants/comment2.html', context)


def cookie_save(request):
    context = {}
    if request.COOKIES:
        context = {
            'cookies': request.COOKIES
        }

    if request.method == "POST":
        # response = HttpResponse('Set your cookie_key:'+request.POST['cookie_key']
                                # + 'value:' + request.POST['cookie_value'])

        # response = render(request, 'restaurants/cookie_save.html').

        response = HttpResponseRedirect(reverse('restaurant:cookie_save'))

        response.set_cookie(
            request.POST['cookie_key'], request.POST['cookie_value'], max_age=30)
        # max_age 設定有效期限

        # response.delete_cookie('123') #刪除

        return response
    else:
        return render(request, 'restaurants/cookie_save.html', context)


def cookie_delete(request, key):
    if request.method == "POST":
        response = HttpResponseRedirect(reverse('restaurant:cookie_save'))
        response.delete_cookie(key)
        return response


def session_save(request):
    # django 會將session資訊存入database中我們可以透過ORM指令取得
    # 但session的主健(PK)會透過使用者端的cookie儲存，我們可以投過取得pk來要session資料

    sid = request.COOKIES['sessionid']
    s = Session.objects.get(pk=sid)
    sinfo = "sessionID:"+sid+',Expire_date:' + str(s.expire_date) +\
        ",Date:" + str(s.get_decoded())

    context = {'sinfo': sinfo}
    if request.session:
        context.update({
            'sessions': request.session
        })

    if request.method == 'POST':
        request.session[request.POST['session_key']
                        ] = request.POST['session_value']
        return HttpResponseRedirect(reverse('restaurant:session_save'))

    return render(request, 'restaurants/session_save.html', context)


def session_delete(request, key):
    if request.method == "POST":
        del request.session[key]
        return HttpResponseRedirect(reverse('restaurant:session_save'))


def login(request):
    # return HttpResponse(request)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('restaurant:backend'))

    email = request.POST.get('email', '')
    username = request.POST.get('username', '')

    password = request.POST.get('password', '')
    user = auth.authenticate(email=email, password=password)
    # user = auth.authenticate(username=username, password=password)
    # auth.authenticate方法接受兩個引數username、password
    # 如果帳密正確會回傳具名用戶的User物件
    if user is not None and user.is_active:
        auth.login(request, user)
        # is_active確認該帳戶有沒有被凍結
        # 通過就使用auth.login方法來登入
        return HttpResponseRedirect(reverse('restaurant:backend'))

    return render(request, 'Backend/login.html')


def backend(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('restaurant:login'))
    return render(request, 'Backend/index.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('restaurant:login'))
