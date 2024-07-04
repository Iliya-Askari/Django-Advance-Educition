from django.test import TestCase , Client
from django.urls import reverse
from datetime import datetime

from accounts.models import Profile, User
from blog.models import Post , Category

class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@test.com',password='a/@12345678')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name = 'iliya' ,
            last_name = 'askari', 
            description = 'Test description'
            )
        self.post = Post.objects.create(
            author = self.profile,
            title ="hello",
            content ="how are you",
            status= True,
            category =None,
            published_date= datetime.now(),
        )

    def test_blog_index_view_returns_status_code_200(self):
        url = reverse('blog:fbv-test')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,template_name = "index.html")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail',kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail',kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)