from django.conf.urls import url, include

from crm import views

urlpatterns = [
    # 公户
    # url(r'customer_list', views.customer_list, name='customer'),
    url(r'customer_list/', views.CustomerList.as_view(), name='customer'),
    # 私户
    # url(r'my_customer', views.customer_list, name='my_customer'),
    url(r'my_customer/', views.CustomerList.as_view(), name='my_customer'),
    # # 增加客户
    # url(r'customer/add/', views.add_customer, name='add_customer'),
    # # 编辑客户
    # url(r'customer/edit/(\d+)', views.edit_customer, name='edit_customer')
    
    # 增加客户
    url(r'customer/add/', views.customer, name='add_customer'),
    # 编辑客户
    url(r'customer/edit/(\d+)', views.customer, name='edit_customer')

]
