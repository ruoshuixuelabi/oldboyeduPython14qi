import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django
    django.setup()

    from app01 import models


    # all()   ——》 对象列表
    ret = models.Person.objects.all()
    # print(ret)

    # get ——》 对象
    # 查询不到报错
    # 获取多个就报错
    ret = models.Person.objects.get(id=1)
    # print(ret)

    # filter   查询出所有满足条件的对象  ——》 对象列表
    ret = models.Person.objects.filter(sex=1)
    # print(ret)

    # exclude  查询出所有不满足条件的对象  ——》 对象列表
    ret = models.Person.objects.exclude(id=1)
    # print(ret)

    # values 取具体的数据    —— 》对象列表  元素  {}    字段 ： 值
    # 没有指定参数  获取所有的字段数据
    # 指定参数     获取指定字段数据
    ret = models.Person.objects.all().values('id','name')
    # for i in ret:
    #     print(i,type(i))

    # values_list  取具体的数据    —— 》对象列表  元素  ()    值
    # 没有指定参数  获取所有的字段数据
    # 指定参数     获取指定字段数据
    # ret = models.Person.objects.all().values_list('name','id')
    # for i in ret:
    #     print(i,type(i))


    # order_by 排序  可以指定多个字段
    ret = models.Person.objects.all().order_by('age','-id',)
    # print(ret)

    ret =models.Person.objects.all().reverse()
    # print(ret)

    # distinct  去重

    # count 计数
    ret = models.Person.objects.all().count()
    # print(ret)

    ret = models.Person.objects.filter(id=100)
    # print(ret.first())

    ret = models.Person.objects.all().exists()
    print(ret)


"""
返回对象列表的方法
all()
filter()
exclude()
order_by()
reverse()
distinct()
values()  {}
values_list()   ()

返回对象的方法
get()
first()
last()
create()

返回布尔值的
exists()

返回数字的
count()




"""