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
    def detail(cls, advert_id) -> Advert:
        """Get advert."""
        try:
            advert = Advert.objects.select_related('city', 'category').get(id=advert_id)
        except Advert.DoesNotExist as exc:
            raise cls.AdvertNotFoundError() from exc

        advert.views += 1
        advert.save()

        return advert
