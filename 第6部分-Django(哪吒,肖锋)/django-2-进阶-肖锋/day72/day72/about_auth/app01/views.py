from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app01.forms import RegForm
from django.contrib.auth.models import User,AbstractUser


def login(request):
    if request.method == 'POST':
        # 方法一
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = auth.authenticate(request, username=username, password=password)
        # 方法二
        # request.POST.pop('csrfmiddlewaretoken')
        # obj = auth.authenticate(request, **request.POST)
        # print(obj)
        if obj:
            # 记录登录状态
            auth.login(request, obj)

            next = request.GET.get('next')

            if next:
                return redirect(next)
            return redirect('/index/')

    # 返回登录页面
    return render(request, 'login.html')


# @login_required
def index(request):
    # 登录状态
    # print(request.user.is_authenticated())

    print(request.user.password)

    if request.user.check_password('root1234'):

        request.user.set_password('admin1234')
        request.user.save()
    return render(request, 'index.html')


# 注销
def logout(request):
    auth.logout(request)

    return redirect('/login/')


def reg(request):
    form_obj = RegForm()

    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 数据库操作
            # username = form_obj.cleaned_data.get('username')
            # password = form_obj.cleaned_data.get('password')

            # User.objects.create(username=username,password=password)

            form_obj.cleaned_data.pop('re_password')
            # User.objects.create_user(is_staff=1, **form_obj.cleaned_data)

            # 创建超级用户
            User.objects.create_superuser(email='', **form_obj.cleaned_data)

            return redirect('/login/')

    return render(request, 'reg.html', {'form_obj': form_obj})
