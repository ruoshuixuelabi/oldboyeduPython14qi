from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac import models
from rbac.forms import *
from django.db.models import Q


def role_list(request):
    all_roles = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {"all_roles": all_roles})


def role(request, edit_id=None):
    obj = models.Role.objects.filter(id=edit_id).first()
    form_obj = RoleForm(instance=obj)
    if request.method == 'POST':
        form_obj = RoleForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:role_list'))
    
    return render(request, 'rbac/form.html', {'form_obj': form_obj})


def del_role(request, del_id):
    models.Role.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:role_list'))


# 菜单信息  权限信息
def menu_list(request):
    all_menu = models.Menu.objects.all()
    
    mid = request.GET.get('mid')
    
    if mid:
        permission_query = models.Permission.objects.filter(Q(menu_id=mid) | Q(parent__menu_id=mid))
    else:
        permission_query = models.Permission.objects.all()
    
    all_permission = permission_query.values('id', 'url', 'title', 'name', 'menu_id', 'parent_id','menu__title')
    
    all_permission_dict = {}
    
    for item in all_permission:
        menu_id = item.get('menu_id')
        if menu_id:
            item['children'] = []
            all_permission_dict[item['id']] = item
    
    for item in all_permission:
        pid = item.get('parent_id')
        
        if pid:
            all_permission_dict[pid]['children'].append(item)
    
    print(all_permission_dict)
    
    return render(request, 'rbac/menu_list.html',
                  {"all_menu": all_menu, 'all_permission_dict': all_permission_dict, 'mid': mid})


def menu(request, edit_id=None):
    obj = models.Menu.objects.filter(id=edit_id).first()
    form_obj = MenuForm(instance=obj)
    if request.method == 'POST':
        form_obj = MenuForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))
    
    return render(request, 'rbac/form.html', {'form_obj': form_obj})
