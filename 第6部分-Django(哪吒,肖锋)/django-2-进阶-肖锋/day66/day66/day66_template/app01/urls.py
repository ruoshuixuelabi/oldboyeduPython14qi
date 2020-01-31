
from django.conf.urls import url

from app01 import views

urlpatterns = [
    url(r'^show_li/', views.show_li,name='show_li'),
    url(r'^home/$', views.show_li),
    # url(r'^home/([0-9]{4})/([0-9]{2})/$', views.home,name='home'),
    url(r'^home/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.home,name='home'),
    # url(r'^home/(?P<month>[0-9]{2})/$', views.home,),

]
