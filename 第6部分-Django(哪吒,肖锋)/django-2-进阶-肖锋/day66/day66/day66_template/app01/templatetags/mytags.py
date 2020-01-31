from django import template

register = template.Library()

@register.inclusion_tag('show_li.html')
def show_li(num):
    return {'num':range(1,num+1)}
