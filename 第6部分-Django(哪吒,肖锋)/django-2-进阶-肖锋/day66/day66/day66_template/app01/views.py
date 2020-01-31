from django.shortcuts import render,HttpResponse,reverse

def show_li(request):
    return render(request,'index.html')


def home(request,*args,year='2018',**kwargs):
    print(year)

    # year = kwargs.get('year')
    # print(year,type(year))
    # print(reverse('show_li',))
    # print(reverse('home',args=('2008','09')),)
    print(reverse('app02:home',kwargs={'year':'2018','month':'10'}),)
    return HttpResponse('这是app01的home')