from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer , CtegorySerializer
from blog.models import Post , Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
# from rest_framework import mixins
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from .pagaitions import DefaultPagination


# Fuction base view
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

# class base view with APIView
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

"""class PostDetail(APIView):
    '''
    getting a detail of posts
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
"""

# class base view with GenericAPIView & MixinView
"""class PostList(GenericAPIView , ListModelMixin , CreateModelMixin):
    '''
    getting list of and create post with generic api view and mixin
    '''
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self , request, *args, **kwargs):
        return self.create(request , *args , **kwargs)
"""

"""class PostDetail(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    '''
    getting a detail of posts and update posts and delete posts with genric api view mixin
    '''
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)"""

# class base view with genericview
"""class PostList(ListCreateAPIView):
    '''
    getting list of posts and createing post with genric-api-view (ListCreateAPIView)
    '''
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status=True)
    """

"""class PostDetail(RetrieveUpdateDestroyAPIView):
    '''
    getting a detail of posts and update posts and delete posts with genric api view (RetrieveUpdateDestroyAPIView)

    '''
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes=[IsAuthenticatedOrReadOnly]
"""

# Examole for view set in CBV
"""class PostViewset(viewsets.ViewSet):
    '''
    This class performs all related operations for posts based on view set
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset , many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(self.queryset , many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
"""

# Examole for model view set in CBV 
class PostModelViewset(viewsets.ModelViewSet):
    '''
    This class performs all related operations for posts based on view set model without defining the function
    '''
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = {'category':['exact','in'],'author':['exact']}
    search_fields = ['title','content']
    ordering_fields = ['published_date']
    
class CategoryModelViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CtegorySerializer