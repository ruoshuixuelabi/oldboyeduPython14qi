from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import versioning
from utils.version import MyVersion

# Create your views here.


class VersionDemo(APIView):
    # versioning_class = MyVersion
    
    def get(self, request):
        print(request.version)
        print(request.versioning_scheme)
        # 根据版本号处理不同业务逻辑
        if request.version == "v2":
            return Response("这是v2的版本返回信息")
        return Response("这是v1的版本返回信息")