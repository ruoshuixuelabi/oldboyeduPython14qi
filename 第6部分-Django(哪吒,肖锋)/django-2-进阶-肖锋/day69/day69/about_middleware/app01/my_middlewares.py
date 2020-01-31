from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse


class MD1(MiddlewareMixin):

    def process_request(self, request):
        # request.s14 = 's14 very good'
        print('这是MD1中的process_request方法')

    def process_response(self, request, response):
        # print(id(request))
        # print(id(response))
        print('这是MD1中的process_response方法')

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        print('这是MD1中的process_view方法')

    def process_exception(self, request, exception):
        # print(exception,type(exception))
        print('这是MD1中的process_exception方法')
        return HttpResponse(str(exception))


    def process_template_response(self,request,response):
        print('这是MD1中的process_template_response方法')

        return HttpResponse('okkkk')

class MD2(MiddlewareMixin):

    def process_request(self, request):
        print('这是MD2中的process_request方法')
        # return HttpResponse('MD2')

    def process_response(self, request, response):
        print('这是MD2中的process_response方法')
        return response


    def process_view(self, request, view_func, view_args, view_kwargs):

        print('这是MD2中的process_view方法')

        # return HttpResponse('MD2中的process_view')

    def process_exception(self, request, exception):
        # print(exception,type(exception))
        print('这是MD2中的process_exception方法')


    def process_template_response(self,request,response):
        print('这是MD2中的process_template_response方法')

        return response

