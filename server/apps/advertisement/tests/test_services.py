import pytest
from pytest_django.asserts import assertQuerySetEqual

from ..services import AdvertService
from .factories import AdvertFactory, CategoryFactory, CityFactory


@pytest.mark.django_db()
class TestAdvertServiceList:
    """Testing method `list` of AdvertService."""

    def test_success(self):
        """Successful getting of advert list."""
        advert_1 = AdvertFactory(
            title='The first advert',
            description='The first description',
            category=CategoryFactory(name='music'),
            city=CityFactory(name='Moscow'),
        )
        advert_2 = AdvertFactory(
            title='The second advert',
            description='The second description',
            category=CategoryFactory(name='animals'),
            city=CityFactory(name='Paris'),
        )

        result = AdvertService.list()

        assertQuerySetEqual(result, [advert_1, advert_2], ordered=False)

    def test_empty_list(self):
        """Adverts don't exist."""
        result = AdvertService.list()

        assertQuerySetEqual(result, [])


@pytest.mark.django_db()
class TestAdvertServiceDetail:
    """Testing method `detail` of AdvertService."""

    def test_success(self):
        """Successful getting of advert object."""
        advert = AdvertFactory()
        assert advert.views == 0
        result = AdvertService.detail(advert_id=advert.id)

        advert.refresh_from_db()

        assert advert.views == 1
        assert result == advert

    def test_no_advert(self):
        """Advert doesn't exist."""
        with pytest.raises(AdvertService.AdvertNotFoundError):
            AdvertService.detail(advert_id=14)

    def test_get_non_existent_advert(self):
        """Query for non-existent advert."""
        advert = AdvertFactory()

        assert advert.views == 0
        with pytest.raises(AdvertService.AdvertNotFoundError):
            AdvertService.detail(advert_id=999)

        advert.refresh_from_db()

        assert advert.views == 0
