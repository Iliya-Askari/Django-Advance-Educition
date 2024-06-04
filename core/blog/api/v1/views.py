from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def post_list(request):
    '''
    show a list of posts for api access
    '''
    posts = Post.objects.filter(status=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view()
def post_detail(request,id):
    '''
    show a detail of posts for api access
    '''
    post = get_object_or_404(Post,pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)