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
# from django.core.mail import send_mail
from mail_templated import send_mail
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from jwt.exceptions import ExpiredSignatureError , InvalidSignatureError

from decouple import config

class RegistrationsApiView(generics.GenericAPIView):
    '''
    registrations user with registrationapiview
    '''
    serializer_class = RegistrationsSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'email': email
            }
            user_obj = get_object_or_404(User, email = email)
            token = self.get_tokens_for_user(user_obj)
            emai_obj = EmailMessage('email/activision_email.tpl', {'token': token}, "user@example.com",to=[email])
            EmailThread(emai_obj).start()
            return Response(data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

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
   
    def get(self, request, *args, **kwargs):
        self.email = 'admin@1admin.com'
        user_obj = get_object_or_404(User, email = self.email)
        token = self.get_tokens_for_user(user_obj)
        emai_obj = EmailMessage('email/hello.tpl', {'token': token}, "user@example.com",to=[self.email])
        EmailThread(emai_obj).start()
        return Response('test email')
    
    def get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class ActivationsConfirmApiView(APIView):
    def get (self, request, token ,*args, **kwargs):
        try:
            token = jwt.decode(token, config('SECRET_KEY'), algorithms=["HS256"])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response({'details':'token has been expired'},status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'details':'token is invalid'},status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk = user_id)
        if user_obj.is_verified:
            return Response({'details':'your account already been verified'})
        user_obj.is_verified = True
        user_obj.save()
        return Response({'details':'your account been verified and activateions successfuly'})
    
class ActivationsRecendApiView(generics.GenericAPIView):
    serializer_class = ActivsionRecendSerializer

    def post(self ,request, *args,**kwargs):
        serializer = ActivsionRecendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data['user']
        token = self.get_tokens_for_user(user_obj)
        emai_obj = EmailMessage('email/activision_email.tpl', {'token': token}, "user@example.com",to=[user_obj.email])
        EmailThread(emai_obj).start()
        return Response({'details':'user activision recend successfully'})


    def get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)