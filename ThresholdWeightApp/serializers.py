from rest_framework import serializers
from ThresholdWeightApp.models import ThresholdWeightModel


class ThresholdWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThresholdWeightModel
        fields = '__all__'
