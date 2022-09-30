from rest_framework import serializers


class LatitudeLongitudeSerializer(serializers.Serializer):
    latitude = serializers.CharField()
    longitude = serializers.CharField()

