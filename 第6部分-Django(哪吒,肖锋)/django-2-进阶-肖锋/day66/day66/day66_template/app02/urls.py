from django.conf.urls import url

from app02 import views

urlpatterns = [

    url(r'^home/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.home, name='home'),

]
