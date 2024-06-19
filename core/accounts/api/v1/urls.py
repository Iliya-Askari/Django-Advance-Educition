from django.urls import path , include
# from rest_framework.authtoken.views import ObtainAuthToken
from . import views

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

app_name='api-v1'


urlpatterns = [
    # regestrations
    path('registrations/',views.RegistrationsApiView.as_view(),name='registrations'),
    # login token
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CoutomDiscardToken.as_view(),name='token-logout'),
    # login jwt
    path('jwt/create/',TokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
    # change password
    # reset password 
]