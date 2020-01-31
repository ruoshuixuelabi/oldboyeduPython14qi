from django.shortcuts import render,reverse,HttpResponse

def home(request,*args,year='2018',**kwargs):
    print(year)

    # year = kwargs.get('year')
    # print(year,type(year))
    # print(reverse('show_li',))
    # print(reverse('home',args=('2008','09')),)
    print(reverse('home',kwargs={'year':'2018','month':'10'}),)
    return HttpResponse('这是app02的home')