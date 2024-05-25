from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.indexView,name='fbv-test'),
    # path("about/", TemplateView.as_view(template_name="index.html"))
    path('cbv-index',views.IndexView.as_view(),name="class-base-view")
]