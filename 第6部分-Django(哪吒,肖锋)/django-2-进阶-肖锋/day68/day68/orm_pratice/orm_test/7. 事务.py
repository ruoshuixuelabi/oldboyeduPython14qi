import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django

    django.setup()

    from app01 import models

    try:
        from django.db import transaction

        with transaction.atomic():
            new_publisher = models.Publisher.objects.create(name="火星出版社1")
            new_publisher = models.Publisher.objects.create(name="火星出版社1")

            int('1sss')
            new_publisher = models.Publisher.objects.create(name="火星出版社1")
            new_publisher = models.Publisher.objects.create(name="火星出版社1")

    except Exception as e:
        print(str(e))
