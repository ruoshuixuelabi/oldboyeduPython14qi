from django.shortcuts import render, redirect
from django.contrib import auth
from crm.forms import RegForm
from crm import models


def login(request):
    err_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = auth.authenticate(request, username=username, password=password)
        if obj:
            return redirect('/index/')
        err_msg = '用户名或密码错误'
    
    return render(request, 'login.html', {'err_msg': err_msg})


# 注册
def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 创建新用户
            # 方法一
            # form_obj.cleaned_data.pop('re_password')
            # models.UserProfile.objects.create_user(**form_obj.cleaned_data)
            
            # 方法二
            obj = form_obj.save()
            obj.set_password(obj.password)
            obj.save()
            
            return redirect('/login/')
    return render(request, 'reg.html', {'form_obj': form_obj})
