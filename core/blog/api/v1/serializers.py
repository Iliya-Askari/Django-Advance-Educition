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
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relaitive_url = serializers.URLField(source="get_absolute_api_url")
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content','snippet', 'status','relaitive_url', 'absolute_url','created_date', 'published_date']
        read_only_fields = ['content',]
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)

class CtegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']