import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from recruitment.models import University
from recruitment.factories import UniversityFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def university():
    return UniversityFactory()


@pytest.mark.django_db
def test_university_list(api_client, university):
    url = reverse('universities-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert university.name in [item['name'] for item in response.data]
