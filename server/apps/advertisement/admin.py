from django.contrib import admin

from .models import Advert, Category, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    """Admin entity of City model."""

    list_display = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    """Admin entity of Category model."""

    list_display = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id', )


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    """Admin entity of Advert model."""

    list_display = ('id', 'title', 'city', 'category', 'created_at', 'views')
    fields = ('id', 'title', 'description', 'city', 'category', 'created_at', 'views')
    readonly_fields = ('id', 'created_at', 'views')
