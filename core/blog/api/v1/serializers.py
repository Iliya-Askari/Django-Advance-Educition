from rest_framework import serializers
from blog.models import Post , Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    '''
    this is a class to define posts for blog app
    '''
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content', 'status', 'created_date', 'published_date']
        read_only_fields = ['content',]

class CtegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']