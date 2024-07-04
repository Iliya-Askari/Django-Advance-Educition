import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime


from accounts.models import User

@pytest.mark.django_db
class TestPostApi:
    client = APIClient()
    def test_get_post_response_200(self):
        url = reverse('blog:api-v1:post-list')
        user = User.objects.create_user(email='testuser', password='testpassword')
        self.client.login(email='testuser', password='testpassword')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_post_create_response_201(self):
        url = reverse('blog:api-v1:post-list')
        user = User.objects.create_user(email='testuser', password='testpassword')
        self.client.login(email='testuser', password='testpassword')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'ststus': True,
            'published_date': datetime.now()
        }
        response = self.client.post(url, data)
        assert response.status_code == 201
