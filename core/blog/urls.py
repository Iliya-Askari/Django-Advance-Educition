from django.urls import path
from .views import IndexView
from django.views.generic import TemplateView
urlpatterns = [
    path('', IndexView,name='fbv-test'),
    path("about/", TemplateView.as_view(template_name="index.html"))
]