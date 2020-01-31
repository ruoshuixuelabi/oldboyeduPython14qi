from django.shortcuts import render, HttpResponse


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
