from django.shortcuts import render, HttpResponse, redirect


def index(request):
    i1, i2, i3 = '', '', ''

    if request.method == 'POST':
        i1 = int(request.POST.get('i1'))
        i2 = int(request.POST.get('i2'))

        i3 = i1 + i2

    return render(request, 'index.html', {
        'i1': i1,
        'i2': i2,
        'i3': i3,
    })


import time


def calc(request):
    print(request.POST)
    i1 = int(request.POST.get('i1'))
    i2 = int(request.POST.get('i2'))

    i3 = i1 + i2
    time.sleep(5)
    return HttpResponse(i3)


def calcs(request):
    print(request.POST)
    i1 = int(request.POST.get('i1'))
    i2 = int(request.POST.get('i2'))

    i3 = i1 + i2
    return HttpResponse(i3)


import json
from django.http import JsonResponse


def ajax_test(request):
    print(request.POST)
    # print(1,request.POST.get('hobby'))
    # print(2,request.POST.get('hobby[]'))
    # print(3,request.POST.getlist('hobby[]'))

    ret = json.loads(request.POST.get('hobby'))

    print(ret[0])

    res = {'status': 200, 'msg': "ok"}

    # return HttpResponse(json.dumps(res))

    int('sss')
    return JsonResponse(res)


from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def csrf_test(request):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('测试成功')

    return render(request, 'csrf_test.html')


# 上传文件
def upload(request):
    if request.is_ajax():

        f1 = request.FILES.get('f1')
        with open(f1.name, 'wb') as f:
            for i in f1.chunks():
                f.write(i)

        return HttpResponse('上传成功')

    return render(request, 'upload.html')


def reg(request):
    return render(request, 'reg.html')


from app01 import models


def check(request):
    name = request.POST.get('xxx')
    obj = models.User.objects.filter(name=name).first()
    if obj:
        return HttpResponse('用户名已存在')
    else:
        return HttpResponse('用户名可以使用')


from django.views import View


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        ret = {'status':0,'msg':''}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(name=user, pwd=pwd).first()
        if obj:
            ret['url'] = '/index/'
            return JsonResponse(ret)

        else:
            ret['status']=1
            ret['msg']='用户名或密码错误'
            return JsonResponse(ret)
