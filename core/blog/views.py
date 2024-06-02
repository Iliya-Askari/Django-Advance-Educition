from django.shortcuts import render , get_object_or_404 
from django.urls import reverse
from .models import Post
from django.views.generic import ListView , DetailView , TemplateView , RedirectView , FormView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

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
    """
    a class based view to show redirect coustoum page
    """
    url = 'https://digikala.com/'

    def get_redirect_url(self, *args , **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class Postlistview(ListView):
    """
    a class based view to show post page
    """
    queryset = Post.objects.filter(status=True).order_by("-id")
    # model = Post
    context_object_name = 'posts'
    paginate_by = 2
    # ordering = "-published_date"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailview(DetailView):
    """
    a class based view to detail post
    """
    model = Post
    
''' Written based on form views
class PostCreateview(FormView): 
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/' 

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreateview(LoginRequiredMixin,CreateView): 
    """
    a class based view to crerate post But if the user was logged in
    """
    # template_name = 'contact.html'
    model = Post
    fields = ['title','content','status','category','published_date']
    # form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditview(LoginRequiredMixin,UpdateView):
    """
    a class based view to Edit(update) post But if the user was logged in
    """
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteview(LoginRequiredMixin,DeleteView):

    """
    a class based view to delete post But if the user was logged in and superuser
    """
    model = Post
    success_url = '/blog/post/'
    # def get(self, request, *args, **kwargs):
    #     # بررسی کنید که آیا کاربر سوپر یوزر است یا نه
    #     if not request.user.is_superuser:
    #         return HttpResponseForbidden("You do not have permission to view this page.")
        
    #     # اگر کاربر سوپر یوزر است، ادامه دهید و صفحه را نمایش دهید
    #     return render(request, 'post_confirm_delete.html')

