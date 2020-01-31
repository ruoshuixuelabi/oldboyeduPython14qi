from django.db import models


# 书
class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    memo = models.TextField(null=True)
    # 创建外键，关联publish
    publisher = models.ForeignKey(to="Publisher",related_name='books',related_query_name='book')
    # 创建多对多关联author
    author = models.ManyToManyField(to="Author")

    def __str__(self):
        return "<Book object: {} {}>".format(self.id, self.title)


# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return "<Publisher object: {} {}>".format(self.id, self.name)


# 作者
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)

    # sex = models.IntegerField(choices=((1, '男'), (2, '女')))
    # author_detail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return "<Author object: {} {}>".format(self.id, self.name)

#
# class AuthorDetail(models.Model):
#     bitrh = models.DateTimeField(auto_now_add=True)
#     blood = models.CharField()


