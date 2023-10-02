from rest_framework import serializers


class AdvertSerializer(serializers.Serializer):
    """Serializer for advert."""

    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    title = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')
    views = serializers.IntegerField()
