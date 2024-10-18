from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
import pytest
from messaging.models import Thread
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestApi:
    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def create_user(self):
        def _create_user(username, password):
            return User.objects.create_user(username=username,
                                            password=password)

        return _create_user

    @pytest.fixture
    def thread_obj(self, create_user):
        user = create_user("testuser", "password")
        user1 = create_user("test", "password")
        thread = Thread.objects.create(created=timezone.now(),
                                       updated=timezone.now())
        thread.participants.set([user, user1])
        return thread

    @pytest.fixture
    def authenticated_user(self, client):
        def authenticate_user(user):
            client.force_authenticate(user)

        return authenticate_user

    @pytest.fixture
    def threads_url(self):
        return reverse("thread-list")

    @pytest.fixture
    def thread_url(self, thread_obj):
        return reverse("thread-detail",
                       kwargs={"pk": thread_obj.pk})

    def test_get_threads(self, client, authenticated_user, create_user, threads_url):
        user = create_user(username="GetUserPosts", password="password")
        authenticated_user(user)
        response = client.get(threads_url)
        assert response.status_code == status.HTTP_200_OK

    def test_get_thread_denied(self, client, authenticated_user, thread_url, create_user):
        user = create_user(username="GetUserPosts", password="password")
        authenticated_user(user)
        response = client.get(thread_url)
        assert response.status_code == 405

    def test_delete_thread(self, client, authenticated_user, thread_url):
        user = User.objects.get(username="testuser")
        authenticated_user(user)
        response = client.delete(thread_url)
        assert Thread.objects.all().count() == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
class Test_Models:
    @pytest.fixture
    def create_user(db):
        def _create_user(username, email, password):
            return User.objects.create(
                username=username, email=email, password=password
            )

        return _create_user

    def test_user_creating(self, create_user):
        create_user(username="testUser", email="testgmail.com", password="1234")
        assert User.objects.all().count() == 1

    def test_thread_creating(self, create_user):
        user1 = create_user(username="testUser", email="testgmail.com", password="1234")
        user2 = create_user(username="testser", email="testgmail.com", password="1234")
        thread = Thread.objects.create(created=timezone.now(), updated=timezone.now())
        thread.participants.set([user1, user2])
        assert Thread.objects.all().count() == 1
