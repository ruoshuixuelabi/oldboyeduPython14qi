from django.shortcuts import render, HttpResponse
import traceback
from app02 import models
# Create your views here.
import logging
logger = logging.getLogger(__name__)
kangchen = logging.getLogger('kangchen')


def home(request):
    logger.debug('嘿嘿嘿')
    kangchen.warning('哈哈哈')

    # try:
    #
    # except Exception as e:
    #     logger.error(traceback.format_exc())
    ret1 = models.Boy.objects.all()
    ret2 = models.Boy.objects.first().girl_set.all()
    print(ret1, ret2)
    return render(request, '箭头函数.html')


def test1(request):
    return HttpResponse("康琛")


def test2(request):
    return HttpResponse("123")
