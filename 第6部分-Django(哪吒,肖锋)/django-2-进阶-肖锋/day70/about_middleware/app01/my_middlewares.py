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

    def process_template_response(self, request, response):
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

    def process_template_response(self, request, response):
        print('这是MD2中的process_template_response方法')

        return response


import datetime


class IpCount(MiddlewareMixin):
    # 设置访问IP池
    IP_DICT = {}

    """
    IP_DICT  = 
     {'127.0.0.1':
             {'count': 0,
               'time': datetime.datetime.now() + datetime.timedelta(minutes=1) }
     }
    
    """

    def process_request(self, request):
        # 记录每次访问的IP
        ip_name = request.META.get('REMOTE_ADDR')
        # 如果该IP在IP池内则执行以下代码
        if ip_name in self.IP_DICT:
            # 获取该IP的超时时间点
            setted_time = self.IP_DICT.get(ip_name).get('time')
            # 获取当前的访问时间点
            now = datetime.datetime.now()
            # 获取已经访问的次数
            visit_count = self.IP_DICT.get(ip_name).get('count')
            # 当前访问次数是在已经访问的次数+1
            new_count = visit_count + 1
            # 如果当前访问次数小于3次并且当前访问时间点小于超时时间点，可以继续访问并记录访问次数
            if new_count <= 3 and now <= setted_time:
                self.IP_DICT.get(ip_name)['count'] = new_count
                return
            # 如果当前访问时间点超过超时时间点，将该访问IP从IP池删除并可以继续访问
            elif now > setted_time:
                del self.IP_DICT[ip_name]
                return
            # 如果当前访问次数大于3次并且当前访问时间点小于超时时间点，将剩余时间返回给请求者
            elif new_count > 3 and now <= setted_time:
                delta = setted_time - now
                msg = '<h1 style="text-align:center;color:red;">您的访问过于频繁,请于{}秒后访问</h1>'.format(delta.seconds)
                return HttpResponse(msg)
        # 将新IP添加进IP池，并记录当前的第一次访问和一分钟后的时间即超时时间点
        else:
            self.IP_DICT.setdefault(ip_name, {'count': 0,
                                              'time': datetime.datetime.now() +
                                                      datetime.timedelta(minutes=1)})
            return


visit_dict = {}

import time


class Throttle(MiddlewareMixin):

    def process_request(self, request):
        # 1. 获取IP
        ip = request.META.get('REMOTE_ADDR')
        # 2. 有访问记录

        now = time.time()
        if not visit_dict.get(ip):
            visit_dict[ip] = []

        history = visit_dict[ip]

        # 127.0.0.1:[  9:26:15,  9:26:08    9:26:05 ]
        # 3. 根据访问记录做判断

        # 方法一：
        # l = []
        # for i in history:
        #     if now - i < 5:
        #         l.append(i)
        #
        # visit_dict[ip] = l
        #
        # history = visit_dict[ip]

        while history and now - history[-1]>5:
            history.pop()

        if len(history) > 2:
            return HttpResponse('你的频率太快了')

        history.insert(0, now)

        print(history)
