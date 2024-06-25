from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)
from accounts.models import *
from django.core.mail import send_mail
class RegistrationsApiView(generics.GenericAPIView):
    '''
    registrations user with registrationapiview
    '''
    serializer_class = RegistrationsSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
            }
            return Response(data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CustomObtainAuthToken(ObtainAuthToken):
    '''
    obtain auth token for api access 
    '''
    serializer_class = CoustoumAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class CoutomDiscardToken(APIView):
    '''
    login obtain a discardtoken with the api
    '''
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    '''
    create a jwt  for login
    '''
    serializer_class = CoustoumTokenObtainPairSerializer

class ChangePasswordApiView(generics.GenericAPIView):
    model = get_user_model
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer
    def get_object(self):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong  password']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            respone = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message' : 'password updated successfully',
                'data': []
            }
            return Response(respone)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileApiSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

class TestEmailSendView(APIView):
    def post(self, request, *args, **kwargs):
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )
        return Response('test email')