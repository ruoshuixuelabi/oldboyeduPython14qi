from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
from .models import Book, Publisher
import json

# Create your views here.
# book_list = [
#     {
#         id: 1,
#         "title": "xx",
#         "publisher": {
#                 "id": 1,
#                 "title": "xx"
#              }
#     }
# ]

# 第一版用values方法取数据
# class BookView(View):
#     def get(self, request):
#         book_queryset = Book.objects.values("id", "title","pub_time", "publisher")
#         book_list = list(book_queryset)
#         ret = []
#         for book in book_list:
#             book["publisher"] = {
#                 "id": book["publisher"],
#                 "title": Publisher.objects.filter(id=book["publisher"]).first().title,
#             }
#             ret.append(book)
#         # ret = json.dumps(book_list, ensure_ascii=False)
#         # return HttpResponse(ret)
#         return JsonResponse(ret, safe=False, json_dumps_params={"ensure_ascii": False})

# 第二版 django的序列化
class BookView(View):
    def get(self, request):
        book_queryset = Book.objects.all()
        data = serializers.serialize("json", book_queryset, ensure_ascii=False)
        return HttpResponse(data)