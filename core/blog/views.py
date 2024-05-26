from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.views.generic.base import TemplateView , RedirectView
from .models import Post
from django.utils import timezone
from django.views.generic.list import ListView
# Create your views here.


# Function Base View Show a template 
'''
def indexView(request):
    """
    a function based view to show index page
    """
    name = 'ali'
    context = {'name':name}
    return render(request, 'index.html', context)
'''

'''
from django.shortcuts import redirect
def redirectTodigi(request):
    return redirect('https://digikala.com/')
'''    

class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context ["name"] = 'ali'
        context ['posts'] = Post.objects.all()
        return context

class RedirectTodigi(RedirectView):
    url = 'https://digikala.com/'

    def get_redirect_url(self, *args , **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class Postlist(ListView):
    queryset = Post.objects.filter(status=False).order_by("-id")
    # model = Post
    context_object_name = 'posts'
    paginate_by = 2
    # ordering = "-published_date"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts