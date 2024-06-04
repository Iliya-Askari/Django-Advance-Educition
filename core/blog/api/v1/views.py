from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def post_list(request):
    '''
    show a list of posts for api access
    '''
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def post_detail(request,id):
    '''
    show a detail of posts for api access
    '''
    if request.method == 'GET':
        post = get_object_or_404(Post,pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == 'PUT':
        post = get_object_or_404(Post,pk=id)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)