# -*- coding: utf-8 -*-
# __author__ = "maple"


import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    import django
    django.setup()

    from app02.models import Student
    # for i in range(500):
    #     Student.objects.create(name=f'康琛{i}')
    #
    # 批量创建
    objs = (Student(name=f'康琛{i}') for i in range(500))
    Student.objects.bulk_create(objs)

