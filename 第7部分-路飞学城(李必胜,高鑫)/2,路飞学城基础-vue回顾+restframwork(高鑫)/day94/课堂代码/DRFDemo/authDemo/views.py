from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework import versioning
from rest_framework.response import Response
from .models import User
from .auth import MyAuth
from .permission import MyPermission
import uuid
from rest_framework import permissions
from .throttle import MyThrottle, DRFThrottle
from rest_framework import throttling

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        name = request.data.get("name", "")
        pwd = request.data.get("pwd", "")
        # 校验用户名和密码是否正确
        user_obj = User.objects.filter(name=name, pwd=pwd).first()
        if user_obj:
            user_obj.token = uuid.uuid4()
            user_obj.save()
            return Response(user_obj.token)
        else:
            return Response("用户名或密码错误")


class TestView(APIView):
    authentication_classes = [MyAuth, ]
    def get(self, request):
        return Response("测试认证组件")


class TestPermission(APIView):
    authentication_classes = [MyAuth, ]
    permission_classes = [MyPermission, ]
    throttle_classes = [DRFThrottle, ]

    def get(self, request):
        return Response("vip用户能看的电影")







