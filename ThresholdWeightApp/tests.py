from rest_framework import status
from rest_framework.test import APITestCase

from ThresholdWeightApp.models import ThresholdWeightModel


class ThresholdWeightTestCase(APITestCase):
    def test_create_threshold_weight(self):
        data = {"requests_threshold": 10, "price_coefficient": 2.1}
        response = self.client.post("/threshold-weight/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existed_threshold_weight(self):
        ThresholdWeightModel.objects.create(requests_threshold=10, price_coefficient=2.1)
        data = {"requests_threshold": 10, "price_coefficient": 5}
        response = self.client.post("/threshold-weight/create/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_threshold_weight(self):
        ThresholdWeightModel.objects.create(requests_threshold=10, price_coefficient=2.1)
        response = self.client.delete("/threshold-weight/delete/10")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_of_threshold_weight(self):
        response = self.client.get("/thresholds-weights/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_threshold_weight(self):
        ThresholdWeightModel.objects.create(requests_threshold=10, price_coefficient=2.1)
        data = {"requests_threshold": 10, "price_coefficient": 5}
        response = self.client.put("/threshold-weight/update/10", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
