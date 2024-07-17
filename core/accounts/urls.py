from django.urls import path, include
from django.contrib.auth import views

from . import views as view

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("send-email/", view.send_email, name='send-email'),
    path("test/",view.test,name='test'),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
]
