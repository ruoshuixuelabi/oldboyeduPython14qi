# -*- coding: utf-8 -*-
# __author__ = "maple"
from django.conf.urls import url, include
from django.contrib import admin
from .views import LoginView, TestView, TestPermission

urlpatterns = [
    url(r'^login', LoginView.as_view()),
    url(r'^test',TestView.as_view()),
    url(r'^permission',TestPermission.as_view()),
]