from django.urls import path

from . import views

urlpatterns = [
    path('advert-list', views.AdvertListApi.as_view(), name='list'),
    path('advert/<int:advert_id>', views.AdvertDetailApi.as_view(), name='detail'),
]
