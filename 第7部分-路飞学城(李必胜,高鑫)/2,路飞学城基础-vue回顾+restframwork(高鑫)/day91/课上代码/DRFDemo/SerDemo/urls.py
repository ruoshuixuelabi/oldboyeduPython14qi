from django.conf.urls import url, include
from .views import BookView


urlpatterns = [
    url(r'^book', BookView.as_view()),
    
]