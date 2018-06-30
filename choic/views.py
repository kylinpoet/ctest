from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .models import Choices
from .models import Cresult

# Create your views here.

def index(request):

    ci=Choices.objects.filter(bodyselect__contains='selected').order_by('bssort')
    cc=ci.count() #选取的条数
    user=request.user
    student=user.first_name


    return render(request,'choic/index.html',locals())

def saveresult(request):
    if request.method == "GET":
        get_data=request.GET.keys()
        d_list=[]
        for x in get_data:
            d_list.append(x)
        return HttpResponse(get_data.get(d_list[2]))

        id = int(i)
        question = Choices.objects.get(id=id)
        user = request.user
        answer = request.GET.get('answer+i')
        #answerdetail = request.GET.get('answerdetail')
        answerstate = (answer == question.rightanswer)
        Cresult.objects.update_or_create(question=question, user=user, answer=answer,
                                      answerstate=answerstate)

        return  HttpResponseRedirect("/")


def loginstu(request):
    stu=request.GET.get('stu')
    psw=request.GET.get('psw')
    user=authenticate(username=stu,password=psw)
    login(request,user)

    return HttpResponseRedirect("/")
    #return HttpResponse('你的名字%s'%user)