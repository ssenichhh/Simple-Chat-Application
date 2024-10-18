import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client


@pytest.mark.django_db
class TestAuthSystem:

    @pytest.fixture
    def client(self):
        return Client()

    @pytest.fixture
    def create_user(self):
        def _create_user(username, password):
            return User.objects.create_user(username=username, password=password)

        return _create_user

    def test_login_fake_user(self, client):
        response = client.post(
            reverse("login"),
            {"username": "fakeuser", "password": "fakepassword"},
            follow=True,
        )
        assert response.status_code == 200
        assert not User.objects.filter(username="fakeuser").exists()

    def test_login_user(self, client, create_user):
        create_user("testlogin", "testpassword")
        response = client.post(
            reverse("login"),
            {"username": "testlogin", "password": "testpassword"},
            follow=True,
        )
        assert response.status_code == 200
        assert User.objects.filter(username="testlogin").exists()

    def test_register_user(self, client):
        response = client.post(
            reverse("signupuser"),
            {
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            },
            follow=True,
        )
        assert response.status_code == 200
        assert User.objects.filter(username="testuser").exists()

    def test_register_fake_user(self, client):
        response = client.post(
            reverse("signupuser"),
            {
                "username": "fakeuser",
                "password1": "",
                "password2": "",
            },
            follow=True,
        )
        assert response.status_code == 200
        assert not User.objects.filter(username="fakeuser").exists()

    def test_logout_fake_user(self, client):
        response = client.get(reverse("logout"), follow=True)
        assert response.status_code in [200, 303]
        assert not client.session.keys()

    def test_logout_user(self, client, create_user):
        create_user("LogoutUser", "logoutpassword")
        client.login(username="LogoutUser", password="logoutpassword")
        assert client.session
        response = client.post(reverse("logout"), follow=True)
        assert response.status_code in [200, 303]
        assert not client.session.keys()
