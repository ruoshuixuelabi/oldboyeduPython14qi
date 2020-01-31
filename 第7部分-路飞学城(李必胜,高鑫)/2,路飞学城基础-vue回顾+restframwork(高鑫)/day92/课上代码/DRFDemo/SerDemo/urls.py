from django.conf.urls import url, include
from .views import BookView, BookEditView


urlpatterns = [
    url(r'^book$', BookView.as_view()),
    url(r'^book/(?P<id>\d+)', BookEditView.as_view()),
    
]