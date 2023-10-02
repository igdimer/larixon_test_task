from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..advertisement.services import AdvertService
from .serializers import AdvertSerializer


class AdvertListApi(APIView):
    """API for getting Adverts list."""

    def get(self, request: Request) -> Response:  # noqa: D102
        adverts = AdvertService.list()
        data = AdvertSerializer(adverts, many=True).data

        return Response(data)


class AdvertDetailApi(APIView):
    """API for getting Advert detail."""

    def get(self, request: Request, advert_id: int) -> Response:  # noqa: D102
        try:
            advert = AdvertService.detail(advert_id=advert_id)
        except AdvertService.AdvertNotFoundError as exc:
            raise NotFound() from exc

        data = AdvertSerializer(advert).data
        return Response(data)
