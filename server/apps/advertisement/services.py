from django.db.models import F
from django.db.models.query import QuerySet

from ..core.exceptions import BaseServiceError
from .models import Advert


class AdvertService:
    """Service for working with adverts."""

    class AdvertNotFoundError(BaseServiceError):
        """Advert with provided id is not found."""

    @classmethod
    def list(cls) -> QuerySet[Advert]:
        """Get list of adverts."""
        adverts = Advert.objects.all().select_related('city', 'category')
        return adverts

    @classmethod
    def detail(cls, advert_id) -> Advert | None:
        """Get advert."""
        qs = Advert.objects.select_related('city', 'category').filter(id=advert_id)
        if not qs:
            raise cls.AdvertNotFoundError()

        qs.update(views=F('views') + 1)
        advert = qs.first()

        return advert
