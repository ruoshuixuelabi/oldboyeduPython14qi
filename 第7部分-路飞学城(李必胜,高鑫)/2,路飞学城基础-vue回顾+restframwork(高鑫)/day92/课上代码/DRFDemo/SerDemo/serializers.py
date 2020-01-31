from rest_framework import serializers
from djangoDemo.models import Book



class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


def my_validate(value):
    print(1111)
    if "敏感信息" in value.lower():
        raise serializers.ValidationError("有敏感词汇")
    return value

#
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32, validators=[my_validate,])
#     pub_time = serializers.DateField()
#     category = serializers.CharField(source="get_category_display", read_only=True)
#     post_category = serializers.IntegerField(write_only=True)
#
#     publisher = PublisherSerializer(read_only=True)
#     # 内部通过外键关系的id找到了publisher_obj
#     # PublisherSerializer(publisher_obj)
#     authors = AuthorSerializer(many=True, read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#         # validated_data 校验通过的数据 就是book_obj
#         # 通过ORM操作给Book表增加数据
#         print(validated_data)
#         book_obj = Book.objects.create(title=validated_data["title"], pub_time=validated_data["pub_time"], category=validated_data["post_category"], publisher_id=validated_data["publisher_id"])
#         print(book_obj)
#         book_obj.authors.add(*validated_data["author_list"])
#         return book_obj
#
#     def update(self, instance, validated_data):
#         # instance 更新的book_obj 对象
#         # validated_data 校验通过的数据
#         # ORM做更新操作
#         instance.title = validated_data.get("title", instance.title)
#         instance.pub_time = validated_data.get("pub_time", instance.pub_time)
#         instance.category = validated_data.get("post_category", instance.category)
#         instance.publisher_id = validated_data.get("publisher_id", instance.publisher_id)
#         if validated_data.get("author_list"):
#             instance.authors.set(validated_data["author_list"])
#         instance.save()
#         return instance
#
#     def validate_title(self, value):
#         print(2222)
#         # value就是title的值 对value处理
#         if "python" not in value.lower():
#             raise serializers.ValidationError("标题必须含有python")
#         return value
#
#     def validate(self, attrs):
#         print(33333)
#         # attrs 字典有你传过来的所有的字段
#         print(attrs)
#         if "python" in attrs["title"].lower() or attrs["post_category"] == 1:
#             return attrs
#         else:
#             raise serializers.ValidationError("分类或标题不合符要求")


class BookSerializer(serializers.ModelSerializer):
    # category_display = serializers.SerializerMethodField(read_only=True)
    # # publisher_info = serializers.SerializerMethodField(read_only=True)
    # # authors_info = serializers.SerializerMethodField(read_only=True)
    #
    # def get_category_display(self, obj):
    #     # obj 就是序列化的每个Book对象
    #     return obj.get_category_display()
    publisher_info = serializers.SerializerMethodField(read_only=True)
    authors_info = serializers.SerializerMethodField(read_only=True)
    
    def get_authors_info(self, obj):
        authors_querset = obj.authors.all()
        return [{"id": author.id, "name": author.name} for author in authors_querset]
    
    def get_publisher_info(self, obj):
        publisher_obj = obj.publisher
        return {"id": publisher_obj.id, "title": publisher_obj.title}
    
    class Meta:
        model = Book
        fields = "__all__"
        # exclude=["id"]
        # 会让你这些所有的外键关系变成read_only = True
        # depth = 1
        extra_kwargs = {"publisher": {"write_only": True}, "authors":{"write_only": True}}
