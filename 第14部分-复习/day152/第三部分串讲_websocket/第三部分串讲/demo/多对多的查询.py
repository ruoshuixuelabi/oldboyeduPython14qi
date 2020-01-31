# -*- coding: utf-8 -*-
# __author__ = "maple"

import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    import django
    django.setup()

    from app02.models import B2G, Boy
    # 男孩1和女孩2的所有约会记录
    ret1 = B2G.objects.filter(boy_id=1, girl_id=2)
    print(ret1.defer('date'))
    # 男孩1都约过的所有女孩的姓名?
    ret2 = Boy.objects.filter(id=1).values('girl__name')
    print(ret2)

    boy_obj = Boy.objects.filter(id=1).first()
    ret3 = boy_obj.girl_set.all()
    print(ret3)


