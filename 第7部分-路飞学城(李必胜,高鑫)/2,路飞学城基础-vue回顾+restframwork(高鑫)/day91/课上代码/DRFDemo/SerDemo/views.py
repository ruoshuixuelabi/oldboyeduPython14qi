from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from djangoDemo.models import Book
from .serializers import BookSerializer


# Create your views here.

class BookView(APIView):
    def get(self, request):
        book_queryset = Book.objects.all()
        # [book_obj, ]
        # 用序列化器进行序列化
        ser_obj = BookSerializer(book_queryset, many=True)
        return Response(ser_obj.data)

    def post(self, request):
        pass