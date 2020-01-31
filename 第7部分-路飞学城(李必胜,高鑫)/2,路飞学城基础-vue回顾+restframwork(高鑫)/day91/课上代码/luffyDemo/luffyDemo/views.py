from django.http import HttpResponse
from django.views import View


def my_demo(request):
    return HttpResponse("ok")

class MyView(View):
    def get(self, request):
        pass

