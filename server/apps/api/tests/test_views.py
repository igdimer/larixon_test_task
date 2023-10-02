import pytest
from django.urls import reverse

from server.apps.advertisement.services import AdvertService


@pytest.mark.django_db()
class TestAdvertListApi:
    """Testing AdvertListApi."""

    def test_success_response(self, client, mock_list, advert):
        """Success response."""
        response = client.get(reverse('list'))

        mock_list.assert_called()
        assert response.status_code == 200
        assert response.json() == [
            {
                'created_at': advert.created_at.strftime('%Y-%m-%d %H:%M'),
                'title': 'Test advert',
                'description': 'Test description',
                'city': 'London',
                'category': 'cars',
                'views': 0,
            },
        ]

    def test_method_not_allowed(self, client):
        """Incorrect HTTP method."""
        response = client.post(reverse('list'))

        assert response.status_code == 405
        assert response.json() == {
            'detail': 'Method "POST" not allowed.',
        }

    def test_internal_error(self, client, mock_list):
        """Internal error."""
        mock_list.side_effect = Exception()
        response = client.get(reverse('list'))

        assert response.status_code == 500
        assert response.json() == {
            'detail': 'Internal Server Error',
        }


@pytest.mark.django_db()
class TestAdvertDetailApi:
    """Testing AdvertDetailApi."""

    def test_success_response(self, client, mock_detail, advert):
        """Success response."""
        response = client.get(reverse('detail', args=[2]))

        mock_detail.assert_called_with(advert_id=2)
        assert response.status_code == 200
        assert response.json() == {
            'created_at': advert.created_at.strftime('%Y-%m-%d %H:%M'),
            'title': 'Test advert',
            'description': 'Test description',
            'city': 'London',
            'category': 'cars',
            'views': 0,
        }

    def test_not_found(self, client, mock_detail):
        """Advert is not found."""
        mock_detail.side_effect = AdvertService.AdvertNotFoundError()
        response = client.get(reverse('detail', args=[2]))

        mock_detail.assert_called_with(advert_id=2)
        assert response.status_code == 404
        assert response.json() == {
            'detail': 'Not found.',
        }

    def test_method_not_allowed(self, client):
        """Incorrect HTTP method."""
        response = client.post(reverse('detail', args=[2]))

        assert response.status_code == 405
        assert response.json() == {
            'detail': 'Method "POST" not allowed.',
        }

    def test_internal_error(self, client, mock_detail):
        """Internal error."""
        mock_detail.side_effect = Exception()
        response = client.get(reverse('detail', args=[2]))

        assert response.status_code == 500
        assert response.json() == {
            'detail': 'Internal Server Error',
        }
