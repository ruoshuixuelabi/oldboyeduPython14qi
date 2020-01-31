from django.shortcuts import render, HttpResponse,redirect
from app01.forms import RegForm, RegForm2


def register(request):
    name_error = ''
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if len(user) < 6:
            name_error = '你太短了'

        else:
            # 数据时合格的 进行数据的操作
            return HttpResponse('注册成功')

    return render(request, 'register.html', {"name_error": name_error})


def register2(request):
    form_obj = RegForm()
    # print(RegForm.hobby.choices)
    # print(11,form_obj.fields['hobby'].choices)

    if request.method == 'POST':
        form_obj = RegForm(request.POST)

        if form_obj.is_valid():
            # cleaned_data  是经过校验的数据
            print(form_obj.cleaned_data)
            # 数据操作
            return HttpResponse('注册成功')

    return render(request, 'register2.html', {"form_obj": form_obj})


def reg(request):
    form_obj = RegForm2()

    if request.method == 'POST':
        form_obj = RegForm2(request.POST)
        if form_obj.is_valid():
            # 数据库操作
            return redirect('https://www.baidu.com')


    return render(request, 'reg.html', {'form_obj': form_obj})
