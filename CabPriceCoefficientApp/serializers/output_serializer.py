from rest_framework import serializers
from ThresholdWeightApp.models import ThresholdWeightModel


class CabPriceCoefficientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThresholdWeightModel
        exclude = ['requests_threshold']
