from django.conf.urls import url
from .views import CourseCategoryView, CourseView


urlpatterns = [
    url(r'^category$', CourseCategoryView.as_view()),
    url(r'^$', CourseView.as_view()),
   
]