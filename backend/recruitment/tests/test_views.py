import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from accounts.enums import AccountTypes
from recruitment.factories import UniversityFactory, UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def university():
    return UniversityFactory()


@pytest.fixture
def admin():
    return UserFactory(is_staff=True, is_superuser=True, account_type=AccountTypes.ADMIN)


@pytest.mark.django_db
def test_university_list(api_client, university, admin):
    api_client.force_authenticate(user=admin)

    url = reverse('universities-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert university.name in [item['name'] for item in response.data]


@pytest.mark.django_db
def test_university_create(api_client, university, admin):
    api_client.force_authenticate(user=admin)
    data = {
        "name": "1111",
        "owner": admin.id,
        "address": "string",
    }
    url = reverse('universities-list')
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == "1111"