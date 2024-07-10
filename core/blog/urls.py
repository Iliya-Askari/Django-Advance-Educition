from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    # fbv
    path("", views.IndexView.as_view(), name="fbv-test"),
    # path("go-to-index",views.redirectTodigi,name="redirect-to-index"),
    # cbv
    # path("about/", TemplateView.as_view(template_name="index.html")),
    # path('cbv-index',views.IndexView.as_view(),name="cbv-index"),
    # path("go-to-digi/<int:pk>/",views.RedirectTodigi.as_view(),name="redirect-to-digi"),
    # post view
    path("post/", views.Postlistview.as_view(), name="post-list"),
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
    path("post/<int:pk>/", views.PostDetailview.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateview.as_view(), name="post-create"),
    path("post/<int:pk>/edit", views.PostEditview.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete",
        views.PostDeleteview.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
