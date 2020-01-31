from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

"""

"""


class Boy(models.Model):
    title = models.CharField(max_length=32)


class Girl(models.Model):
    name = models.CharField(max_length=32)
    boys = models.ManyToManyField(to='Boy', through='B2G', through_fields=('girl', 'boy'))

    def __str__(self):
        return self.name


class B2G(models.Model):
    boy = models.ForeignKey(to=Boy, on_delete=models.CASCADE)
    girl = models.ForeignKey(to=Girl, on_delete=models.CASCADE)
    date = models.DateField()





