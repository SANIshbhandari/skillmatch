import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_and_login_returns_role():
    c = APIClient()
    r = c.post(
        "/api/auth/register/",
        {"username": "ram", "password": "Pass12345", "role": "recruiter"},
        format="json",
    )
    assert r.status_code == 201
    r = c.post(
        "/api/auth/login/",
        {"username": "ram", "password": "Pass12345"},
        format="json",
    )
    assert r.status_code == 200
    assert r.data["role"] == "recruiter"


@pytest.mark.django_db
def test_cannot_register_as_admin():
    r = APIClient().post(
        "/api/auth/register/",
        {"username": "evil", "password": "Pass12345", "role": "admin"},
        format="json",
    )
    assert r.status_code == 400