from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac.models import User
from app01.models import Student
from rbac.server.init_permission import init_permission

def student_list(request):
    students = Student.objects.all()
    
    return render(request, 'student_list.html', {'students': students})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        
        user = User.objects.filter(name=username, password=pwd).first()
        
        if not user:
            err_msg = '用户名或密码错误'
            
        # 初始化权限和菜单信息
        init_permission(request,user)
        
        return redirect(reverse('student'))
    
    return render(request, 'login.html')
