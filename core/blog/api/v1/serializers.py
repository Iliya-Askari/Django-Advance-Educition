from rest_framework import serializers
from blog.models import Post , Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    '''
    this is a class to define posts for blog app
    '''
    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content', 'status', 'created_date', 'published_date']

class CtegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']