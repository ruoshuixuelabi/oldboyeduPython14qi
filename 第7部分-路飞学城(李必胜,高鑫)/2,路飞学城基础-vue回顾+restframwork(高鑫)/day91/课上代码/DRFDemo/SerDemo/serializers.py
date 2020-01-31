from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)
    pub_time = serializers.DateField()
    category = serializers.CharField(source="get_category_display")
    
    publisher = PublisherSerializer()
    authors = AuthorSerializer(many=True)
    
    
    

