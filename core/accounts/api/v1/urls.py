from django.urls import path , include
# from rest_framework.authtoken.views import ObtainAuthToken
from . import views

app_name='api-v1'


urlpatterns = [
    # regestrations
    path('registrations/',views.RegistrationsApiView.as_view(),name='registrations'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CoutomDiscardToken.as_view(),name='token-logout')
    # login token
    # login jwt
    # change password
    # reset password 
]