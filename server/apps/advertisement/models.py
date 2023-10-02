from django.db import models


class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """Text representation."""
        return self.name


class City(models.Model):
    """City model."""

    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'city'
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        """Text representation."""
        return self.name


class Advert(models.Model):
    """Advert model."""

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    views = models.PositiveIntegerField()

    class Meta:
        db_table = 'advert'
        verbose_name = 'advert'
        verbose_name_plural = 'adverts'

    def __str__(self):
        """Text representation."""
        return self.title
