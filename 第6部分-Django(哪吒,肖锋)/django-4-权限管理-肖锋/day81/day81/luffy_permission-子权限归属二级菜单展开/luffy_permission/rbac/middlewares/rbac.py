from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse
import re


class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 对权限进行校验
        # 1. 当前访问的URL
        current_url = request.path_info
        
        # 白名单的判断
        for i in settings.WHITE_URL_LIST:
            if re.match(i, current_url):
                return
        
        # 2. 获取当前用户的所有权限信息
        
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        # 3. 权限的校验
        print(current_url)
        
        for item in permission_list:
            url = item['url']
            if re.match("^{}$".format(url), current_url):
                pid = item['pid']
                id = item['id']
                if pid:
                    # 表示当前权限是子权限，让父权限是展开
                    request.current_menu_id = pid
                    print()
                else:
                    # 表示当前权限是父权限，要展开的二级菜单
                    request.current_menu_id = id
                return
        
        else:
            return HttpResponse('没有权限')
