from django.shortcuts import render, redirect, HttpResponse


def login_required(fn):
    def inner(request, *args, **kwargs):
        if not request.COOKIES.get('is_login') == '1':
            next = request.path_info
            return redirect('/login/?next={}'.format(next))

        ret = fn(request, *args, **kwargs)

        return ret

    return inner


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == 'alexdsb':
            next = request.GET.get('next')

            if next:
                ret = redirect(next)
            else:
                ret = redirect('/index/')

            ret.set_cookie('is_login', '1', max_age=5)
            return ret

    return render(request, 'login.html')


@login_required
def home(request):
    return HttpResponse('这是home页面')


@login_required
def index(request):
    return render(request, 'index.html')


def logout(request):
    ret = redirect('/login/')

    ret.delete_cookie('is_login')

    return ret
