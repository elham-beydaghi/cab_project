from rest_framework import serializers
from CabPriceRatioProject.CabPriceApp.models import PriceWeightModel


class PriceWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceWeightModel
        fields = '__all__'
