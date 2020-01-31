from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.


class CorsDemoView(APIView):
    def get(self, request):
        return HttpResponse("handlerResponse('ok')")
    
    def post(self, request):
        return HttpResponse("post~ok~~")
    
    def put(self, request):
        return HttpResponse("put~~ok~~")
