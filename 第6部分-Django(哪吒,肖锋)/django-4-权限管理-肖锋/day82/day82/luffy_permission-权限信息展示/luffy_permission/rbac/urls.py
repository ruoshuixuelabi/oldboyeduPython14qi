from django.conf.urls import url
from rbac import views

urlpatterns = [
    # /app01/role/list/    # rbac:role_list
    url(r'^role/list/$', views.role_list, name='role_list'),
    url(r'^role/add/$', views.role, name='role_add'),
    url(r'^role/edit/(\d+)$', views.role, name='role_edit'),
    url(r'^role/del/(\d+)$', views.del_role, name='role_del'),
    
    url(r'^menu/list/$', views.menu_list, name='menu_list'),
    
    url(r'^menu/add/$', views.menu, name='menu_add'),
    url(r'^menu/edit/(\d+)$', views.menu, name='menu_edit'),
]
