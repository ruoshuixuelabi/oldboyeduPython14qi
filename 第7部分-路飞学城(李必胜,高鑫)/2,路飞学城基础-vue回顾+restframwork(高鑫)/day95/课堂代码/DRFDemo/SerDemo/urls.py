from django.conf.urls import url, include
from .views import BookView, BookEditView, BookModelView, PageBookView
# 帮助我们生成带参数的路由
from rest_framework.routers import DefaultRouter
# 实例化DefaultRouter对象
router = DefaultRouter()
# 注册我们的路由以及视图
router.register(r'^book', BookModelView)


urlpatterns = [
    # url(r'^book$', BookView.as_view()),
    # url(r'^book/(?P<id>\d+)', BookEditView.as_view()),
    # url(r'^book$', BookModelView.as_view({"get": "list", "post": "create"})),
    # url(r'^book/(?P<pk>\d+)', BookModelView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    url(r'page_book$', PageBookView.as_view()),
    
]

urlpatterns += router.urls