import factory

from ..models import Advert, Category, City


class CityFactory(factory.django.DjangoModelFactory):
    """City factory."""

    class Meta:
        model = City
        django_get_or_create = ('name',)

    name = 'London'


class CategoryFactory(factory.django.DjangoModelFactory):
    """Category factory."""

    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = 'cars'


class AdvertFactory(factory.django.DjangoModelFactory):
    """Advert factory."""

    class Meta:
        model = Advert

    title = 'Test advert'
    description = 'Test description'
    city = factory.SubFactory(CityFactory)
    category = factory.SubFactory(CategoryFactory)
