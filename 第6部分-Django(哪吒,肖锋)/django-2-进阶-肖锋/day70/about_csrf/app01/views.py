from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.

@csrf_protect
def login(request):
    return render(request, 'login.html')
