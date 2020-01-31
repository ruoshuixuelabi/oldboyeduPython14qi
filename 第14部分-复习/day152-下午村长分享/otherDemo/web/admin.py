from django.contrib import admin

from web import models

admin.site.register(models.Tag)
admin.site.register(models.Comment)
