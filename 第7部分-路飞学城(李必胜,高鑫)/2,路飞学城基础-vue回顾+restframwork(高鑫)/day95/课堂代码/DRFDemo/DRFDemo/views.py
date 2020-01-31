from django.views import View
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


class DemoView(View):
    def get(self, request):
        print(type(request))
        request.POST
        return HttpResponse("ok")
    

from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework import parsers

from rest_framework import permissions