from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post

@api_view()
def post_list(request):
    return Response('ok')

@api_view()
def post_detail(request,id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)