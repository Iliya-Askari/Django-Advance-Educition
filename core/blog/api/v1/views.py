from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status

@api_view()
def post_list(request):
    return Response('ok')

@api_view()
def post_detail(request,id):
    try:
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"detail":"post not found"},status=status.HTTP_404_NOT_FOUND)