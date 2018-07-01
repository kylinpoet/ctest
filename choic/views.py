from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout
from .models import Choices
from .models import Cresult
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

# from datetime import datetime

# Create your views here.
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):

    return render(request,'choic/index.html',locals())

@login_required
def answer(request):


    ci=Choices.objects.filter(bodyselect__contains='selected').order_by('bssort')
    cc=ci.count() #选取的条数
    user=request.user
    student=user.first_name
    if request.session.has_key('answered'):
        dic_answered = request.session['answered']
        for _ in ci:
            dic_answered[str(_.id)] =  {dic_answered.get(str(_.id)):'checked'}
    else:
        dic_answered={}
        for _ in ci:
            dic_answered[str(_.id)] =  {dic_answered.get(str(_.id)):'checked'}

    return render(request, 'choic/answer.html',locals())

@login_required
def saveresult(request):

    if request.method == "GET":
        get_data = request.GET.items()
        request.session['answered'] = dict(request.GET.items())
        for k, v in get_data:
            id1 = int(k)
            question = Choices.objects.get(id=id1)
            user = request.user
            answer = v
            # answerdetail = request.GET.get('answerdetail')
            answerstate = (answer == question.rightanswer)
            Cresult.objects.update_or_create(question=question, user=user, answer=answer,
                                             answerstate=answerstate)
                                             ## answertime=datetime.today().replace(hour=8).isoformat(' '))
        return render(request, 'choic/saveresult.html')
    # return HttpResponseRedirect("/answer/")



def loginstu(request):

    # return render(request, 'choic/loginstu.html', locals())
    if request.method == 'POST':
        stu=request.POST.get('stu')
        psw=request.POST.get('psw')
        user=authenticate(username=stu,password=psw)
        if user is not None:
            login(request, user)  # 登陆成功
            return HttpResponseRedirect('/answer/', {'user': user})
        else:
            return render(request, 'choic/loginstu.html', {'login_error': '用户名或密码错误'})  # 注册失败
    return render(request, 'choic/loginstu.html')


    # return render(request, 'choic/index.html')

        #return render(request, 'choic/index.html')
        #return HttpResponseRedirect("/answer/")
        #return HttpResponse('你的名字%s'%user)

def logoutstu(request):
    logout(request)
    try:
        del request.session['answered']
    except:
        pass
    return HttpResponseRedirect('/')