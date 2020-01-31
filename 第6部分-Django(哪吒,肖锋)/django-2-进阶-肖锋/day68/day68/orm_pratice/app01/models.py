from django.db import models


class MyCharField(models.Field):
    """
    自定义的char类型的字段类
    """

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为max_length指定的值
        """
        return 'char(%s)' % self.max_length


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_column='myname', verbose_name='姓名')
    age = models.IntegerField(null=True, blank=True)
    birth = models.DateTimeField(auto_now=True)
    phone = MyCharField(max_length=11)
    sex = models.CharField(max_length=32, choices=(('1', '男'), ('2', '女')))

    def __str__(self):
        return '< Person %s-%s>' % (self.id, self.name)

    class Meta:
        ordering = ('id',)
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "person"

        # admin中显示的表名称
        verbose_name = '个人信息'

        # verbose_name加s
        verbose_name_plural = '所有用户信息'

        # 联合索引
        # index_together = [
        #     ("pub_date", "deadline"),  # 应为两个存在的字段
        # ]

        # 联合唯一索引
        # unique_together = (("driver", "restaurant"),)  # 应为两个存在的字段


# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=32)  # 出版社名称

    def __str__(self):
        return '<Publisher %s-%s>' % (self.id, self.name)


# 书
class Book(models.Model):
    title = models.CharField(max_length=30)  # 书名
    price = models.IntegerField()  # 价格
    publisher = models.ForeignKey(to='Publisher', null=True)

    sale = models.IntegerField()
    kucun = models.IntegerField()

    def __str__(self):
        return '<Book %s-%s>' % (self.id, self.title)


# 作者
class Author(models.Model):
    name = models.CharField(max_length=32)  # 作者名字
    books = models.ManyToManyField(to='Book', )  # 只是ORM层面建立的一个多对多关系，不是作者表的一个字段

    def __str__(self):
        return self.name
