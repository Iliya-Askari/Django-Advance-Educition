from django.urls import path, include

# from rest_framework.authtoken.views import ObtainAuthToken
from .. import views


urlpatterns = [
    # profile
    path("", views.ProfileApiView.as_view(), name="profile"),
]
