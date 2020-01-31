from django.conf.urls import url, include
from .views import VersionDemo

urlpatterns = [
    url(r'^demo/', VersionDemo.as_view())
]