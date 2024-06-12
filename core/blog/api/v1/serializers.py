from rest_framework import serializers
from blog.models import Post , Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CtegorySerializer(serializers.ModelSerializer):
    '''
    this is a class to define category for blog app
    '''
    class Meta:
        model = Category
        fields = ['id','name']
class PostSerializer(serializers.ModelSerializer):
    '''
    this is a class to define posts for blog app
    '''

    # Testing different read-only methods in the serializer
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    # relaitive_url = serializers.URLField(source="get_absolute_api_url")
    # category = serializers.SlugRelatedField(many=False, slug_field='name',queryset=Category.objects.all())

    absolute_url = serializers.SerializerMethodField()
    snippet = serializers.ReadOnlyField(source='get_snippet')
    class Meta:
        model = Post
        fields = ['id','author', 'title','image' ,'category','content','snippet', 'status', 'absolute_url','created_date', 'published_date']
        # read_only_fields = ['content',]

    def get_absolute_url(self,obj):
        '''
        Get the full address of the posts
        '''
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    
    def to_representation(self, instance):
        '''
        With this method, you can change the method of displaying data in different parts
        '''
        request = self.context.get('request','created_date')
        rep = super().to_representation(instance)

        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet',None)
            rep.pop('absolute_url',None)
            rep.pop('created_date',None)
        else :
            rep.pop('content',None)
        rep ['category'] = CtegorySerializer(instance.category).data
        return rep
