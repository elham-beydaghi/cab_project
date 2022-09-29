from rest_framework import status
from rest_framework.test import APITestCase

from ThresholdWeightApp.models import ThresholdWeightModel


class CabPriceCoefficientTestCase(APITestCase):
    def test_get_cab_price_coefficient_for_not_existed_location(self):
        data = {"lat": "0", "lon": "0"}
        response = self.client.post("/cab-price-coefficient/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
