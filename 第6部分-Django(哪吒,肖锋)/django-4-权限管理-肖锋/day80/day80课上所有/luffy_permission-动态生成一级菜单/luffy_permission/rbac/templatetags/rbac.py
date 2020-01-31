from django import template

register = template.Library()

from django.conf import settings
import re


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    for item in menu_list:
        url = item['url']
        if re.match('^{}$'.format(url), request.path_info):
            item['class'] = 'active'
            break
    
    return {"menu_list": menu_list}
