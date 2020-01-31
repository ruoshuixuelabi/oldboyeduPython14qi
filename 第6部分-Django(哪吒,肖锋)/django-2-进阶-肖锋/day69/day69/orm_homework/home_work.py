import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_homework.settings")
import django

django.setup()

from app01 import models

# 查找所有书名里包含金老板的书
ret = models.Book.objects.filter(title__contains='金老板')
# print(ret)

# 查找出版日期是2018年的书
ret = models.Book.objects.filter(publish_date__year='2018')
# print(ret)

# 查找出版日期是2017年的书名
ret = models.Book.objects.filter(publish_date__year='2017').values('title')
# print(ret)

# 查找价格大于10元的书

ret = models.Book.objects.filter(price__gt=10)
# print(ret)
# 查找价格大于10元的书名和价格
ret = models.Book.objects.filter(price__gt=10).values('title', 'price')
# print(ret)
# 查找memo字段是空的书
from django.db.models import Q

ret = models.Book.objects.filter(Q(memo__isnull=True) | Q(memo=''))
# print(ret)
#
# 查找在北京的出版社
ret = models.Publisher.objects.filter(city='北京')
# print(ret)
# 查找名字以沙河开头的出版社
ret = models.Publisher.objects.filter(name__startswith='沙河')
# print(ret)
#
# 查找“沙河出版社”出版的所有书籍
ret = models.Book.objects.filter(publisher__name='沙河出版社')
# print(ret)

ret = models.Publisher.objects.filter(name='沙河出版社').values('book__title')
# print(ret)

ret = models.Publisher.objects.filter(name='沙河出版社')
for i in ret:
    print(i.books.all())

# 查找每个出版社出版价格最高的书籍价格
from django.db.models import Max, Count

ret = models.Publisher.objects.annotate(Max('book__price')).values()
# print(ret)

# 查找每个出版社的名字以及出的书籍数量
ret = models.Publisher.objects.annotate(count=Count('book')).values('name', 'count')
# print(ret)

#
# 查找作者名字里面带“小”字的作者
# 查找年龄大于30岁的作者
# 查找手机号是155开头的作者
# 查找手机号是155开头的作者的姓名和年龄
#
# 查找每个作者写的价格最高的书籍价格
ret = models.Author.objects.annotate(max=Max('book__price')).values('name', 'max')
# print(ret)

# 查找每个作者的姓名以及出的书籍数量
ret = models.Author.objects.annotate(count=Count('book')).values('name', 'count')
# print(ret)
#
# 查找书名是“跟金老板学开车”的书的出版社
ret = models.Publisher.objects.filter(book__title='跟金老板学开车')
# print(ret)

# 查找书名是“跟金老板学开车”的书的出版社所在的城市
# 查找书名是“跟金老板学开车”的书的出版社的名称

# 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
ret = models.Publisher.objects.filter(book__title='跟金老板学开车').first().books.exclude(title='跟金老板学开车').values('title',
                                                                                                           'price')
print(ret)

ret = models.Book.objects.filter(publisher=models.Publisher.objects.filter(book__title='跟金老板学开车').first()).exclude(
    title='跟金老板学开车')
# print(ret)

#
# 查找书名是“跟金老板学开车”的书的所有作者
# 查找书名是“跟金老板学开车”的书的作者的年龄
# 查找书名是“跟金老板学开车”的书的作者的手机号码
# 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱

ret = models.Author.objects.values('book__title', 'book__price').filter(book__title='跟金老板学开车').distinct()

for i in ret:
    print(i)

# ret = models.Book.objects.get(title='跟金老板学开车').author.values('name', 'book__title', 'book__price').distinct()
# print(ret)

from django.db import transaction

try:
    with transaction.atomic():
        models.Author.objects.create(name='egon', age='xxxx', phone='111111')
        models.Author.objects.create(name='egon1', age=180)

except Exception as e:

    print(str(e))
