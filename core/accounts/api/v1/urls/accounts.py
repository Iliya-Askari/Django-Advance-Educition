from django.urls import path, include

# from rest_framework.authtoken.views import ObtainAuthToken
from .. import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # regestrations
    path("registrations/", views.RegistrationsApiView.as_view(), name="registrations"),
    # path('test-email/',views.TestEmailSendView.as_view(),name='test-email'),
    # activitions
    path(
        "activations/confirm/<str:token>",
        views.ActivationsConfirmApiView.as_view(),
        name="activations",
    ),
    # recend activations
    path(
        "activations/recend/",
        views.ActivationsRecendApiView.as_view(),
        name="activation-recend",
    ),
    # login token
    path("token/login/", views.CustomLoginTokenApiView.as_view(), name="token-login"),
    path(
        "token/logout/", views.CoutomLogoutTokenApiView.as_view(), name="token-logout"
    ),
    # login jwt
    path("jwt/create/", views.CustomCreateJwtApiView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    # change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # reset password
]
