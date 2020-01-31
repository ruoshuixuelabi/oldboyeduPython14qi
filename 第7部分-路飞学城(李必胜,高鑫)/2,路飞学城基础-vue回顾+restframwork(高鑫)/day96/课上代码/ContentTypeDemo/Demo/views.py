from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Food, Fruit, Coupon
from django.contrib.contenttypes.models import ContentType

# Create your views here.


class TestView(APIView):
    def get(self, request):
        # 找到表id以及表对象
        # content_type_obj = ContentType.objects.filter(app_label="Demo", model="food").first()
        # print(type(content_type_obj))
        # model_class = content_type_obj.model_class()
        # print(model_class)
        # print(content_type_obj.id)
        # 给酱香饼创建优惠券
        food_obj = Food.objects.filter(id=1).first()
        Coupon.objects.create(title="酱香饼买一送小威",content_object=food_obj)
        # 给黑美人加优惠券
        # fruit_obj = Fruit.objects.get(id=2)
        # Coupon.objects.create(title="黑美人2折", content_type_id=9, object_id=2)
        # 查询优惠券绑定对象
        # coupon_obj = Coupon.objects.filter(id=1).first()
        # print(coupon_obj.content_object.name)
        # 查某个对象的优惠券
        food_obj = Food.objects.filter(id=1).first()
        print(food_obj.coupons.all())
        return HttpResponse("ok")