from unittest import mock

import pytest
from rest_framework.test import APIClient

from server.apps.advertisement.models import Advert
from server.apps.advertisement.tests.factories import AdvertFactory


@pytest.fixture()
def client():
    """Test client."""
    return APIClient()


@pytest.fixture()
def advert():
    """Advert fixture."""
    return AdvertFactory()


@pytest.fixture()
def mock_list(advert):
    """Mock fixture of method 'list' of AdvertService."""
    with mock.patch('server.apps.advertisement.services.AdvertService.list') as mock_method:
        mock_method.return_value = Advert.objects.all()
        yield mock_method


@pytest.fixture()
def mock_detail(advert):
    """Mock fixture of method 'detail' of AdvertService."""
    with mock.patch('server.apps.advertisement.services.AdvertService.detail') as mock_method:
        mock_method.return_value = advert
        yield mock_method
