import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime

from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def user_client():
    user = User.objects.create_user(email="testuser", password="testpassword")
    return user


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_response_200(self, api_client):
        url = reverse("blog:api-v1:post-list")
        user = User.objects.create_user(email="testuser", password="testpassword")
        api_client.login(email="testuser", password="testpassword")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_post_create_response_401(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "ststus": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_post_create_response_201(self, api_client, user_client):
        url = reverse("blog:api-v1:post-list")
        user = user_client
        api_client.force_login(user=user)
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "ststus": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_post_create_invalid_data_response_400(self, api_client, user_client):
        url = reverse("blog:api-v1:post-list")
        user = user_client
        api_client.force_login(user=user)
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
        }
        response = api_client.post(url, data)
        assert response.status_code == 400
