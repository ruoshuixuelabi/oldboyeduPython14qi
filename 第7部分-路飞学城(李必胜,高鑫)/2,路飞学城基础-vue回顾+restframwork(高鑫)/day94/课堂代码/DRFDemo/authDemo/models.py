from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    token = models.UUIDField(null=True, blank=True)
    type = models.IntegerField(choices=((1, "普通用户"), (2, "vip"),(3, "svip")), default=1)