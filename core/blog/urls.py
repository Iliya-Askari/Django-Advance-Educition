from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='blog'
urlpatterns = [
    # fbv
    # path('', views.indexView,name='fbv-test'),
    # path("go-to-index",views.redirectTodigi,name="redirect-to-index"),

    # cbv 
    # path("about/", TemplateView.as_view(template_name="index.html")),
    path('cbv-index',views.IndexView.as_view(),name="cbv-index"),
    path("post/",views.Postlist.as_view(),name="post-list"),
    path("go-to-digi/<int:pk>/",views.RedirectTodigi.as_view(),name="redirect-to-digi"),
    
]