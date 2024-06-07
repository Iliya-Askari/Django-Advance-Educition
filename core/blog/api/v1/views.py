from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView , ListCreateAPIView
# from rest_framework import mixins
from rest_framework.mixins import ListModelMixin , CreateModelMixin


"""@api_view(['GET', 'POST'])
from rest_framework.decorators import api_view , permission_classes

# @permission_classes([IsAuthenticated])
@permission_classes([IsAuthenticatedOrReadOnly])
# @permission_classes([IsAdminUser])
def post_list(request):
    '''
    show a list of posts for api access
    '''
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        '''
        create of posts for api access
        '''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""    
"""@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,id):
    '''
    show a detail of posts for api access
    '''
    if request.method == 'GET':
        '''
        detail of posts for api access
        '''
        post = get_object_or_404(Post,pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == 'PUT':
        '''
        update of posts for api access
        '''
        post = get_object_or_404(Post,pk=id)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        '''
        delete of posts for api access
        '''
        post = get_object_or_404(Post,pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
"""class PostList(APIView):
    '''
    getting a list of posts and creating posts
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request):
        '''
        show in posts withs CBV 
        '''
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        create in posts withs CBV 
        '''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""
class PostDetail(APIView):
    '''
    getting a detail of posts and creating posts
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request,id):
        '''
        detail in posts withs CBV 
        '''
        post = get_object_or_404(Post,pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        '''
        Update in posts withs CBV 
        '''
        post = get_object_or_404(Post,pk=id)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        '''
        delete in posts withs CBV 
        '''
        post = get_object_or_404(Post,pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostList(ListCreateAPIView):
    '''
    getting list of and create post with genric-api-view (ListCreateAPIView)
    '''
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status=True)
    


