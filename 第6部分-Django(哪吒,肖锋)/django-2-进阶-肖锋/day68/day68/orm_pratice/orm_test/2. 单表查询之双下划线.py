import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django

    django.setup()

    from app01 import models

    ret = models.Person.objects.filter(id__gt=1)  # greater than  大于
    ret = models.Person.objects.filter(id__lt=4)  # less than   小于
    ret = models.Person.objects.filter(id__gte=1)  # greater than equal  大于等于
    ret = models.Person.objects.filter(id__lte=1)  # less than equal  小于等于

    ret = models.Person.objects.filter(id__in=[1, 3])

    ret = models.Person.objects.filter(id__gte=1, id__lte=3)
    ret = models.Person.objects.filter(id__range=[1, 3])

    ret = models.Person.objects.filter(name__contains='e')
    ret = models.Person.objects.filter(name__icontains='e')

    ret = models.Person.objects.filter(name__startswith='e')
    ret = models.Person.objects.filter(name__istartswith='e')

    ret = models.Person.objects.filter(name__endswith='x')
    ret = models.Person.objects.filter(name__iendswith='x')

    # ret = models.Person.objects.filter(birth__year=2018)
    ret = models.Person.objects.filter(birth__day=11)

    print(ret)
