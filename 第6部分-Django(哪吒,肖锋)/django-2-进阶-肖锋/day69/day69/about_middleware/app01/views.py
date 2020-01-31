from django.shortcuts import render, HttpResponse


def index(request,num):
    # print(id(request))
    print('这是index函数')
    print(num)

    # int('xxxx')

    ret = HttpResponse('ok')


    def xxxx():
        print('这是index中的xxxx')
        return HttpResponse('这是index中的xxxx')

    ret.render = xxxx

    print(id(ret))


    return ret
