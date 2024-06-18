from django.urls import path , include
from . import views
app_name='api-v1'


urlpatterns = [
    # regestrations
    path('registrations/',views.RegistrationsApiView.as_view(),name='registrations')
    # login token
    # login jwt
    # change password
    # reset password 
]