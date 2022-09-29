from typing import Dict, Union

from rest_framework.response import Response
from rest_framework import status

from CabPriceCoefficientApp.redis_db import RedisDataBaseAccessObject
from CabPriceCoefficientApp.serializers import CabPriceCoefficientSerializer
from ThresholdWeightApp.models import ThresholdWeightModel

from rest_framework.views import APIView

import hashlib
from geopy.geocoders import Nominatim
import datetime


class CabPriceCoefficientView(APIView):

    def __init__(self):
        super().__init__()
        self.redis_dao = RedisDataBaseAccessObject()

    def post(self, request) -> Response:

        latitude_and_longitude_dict: Dict = request.data
        geolocator = Nominatim(user_agent="snapp_cab_app")
        address_of_the_cab: Dict = \
            geolocator.reverse((latitude_and_longitude_dict['lat'], latitude_and_longitude_dict['lon']), language='en',
                               exactly_one=True).raw['address']
        if address_of_the_cab:
            request_id: str = self._set_request_id_in_redis(latitude_and_longitude_dict, address_of_the_cab)
            serialized_threshold_coefficient_record: CabPriceCoefficientSerializer = \
                self._get_price_coefficient_from_request_threshold(request_id)
            if serialized_threshold_coefficient_record:
                return Response(serialized_threshold_coefficient_record.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _create_request_key_to_store_in_redis(data: dict, address_of_the_cab: dict) -> str:
        data_string: str = str(data)
        data_byte: bytes = data_string.encode('utf_8')
        data_hash: str = hashlib.md5(data_byte).hexdigest()

        now: datetime = datetime.datetime.now()
        date_time_now: str = now.strftime("%Y-%m-%d %H:%M:%S")

        suburb_of_cab_location: str = address_of_the_cab.get("suburb")

        return '{}:{}:{}'.format(suburb_of_cab_location, data_hash, date_time_now)

    def _set_request_id_in_redis(self, data: dict, address_of_the_cab: dict) -> str:
        request_id: str = self._create_request_key_to_store_in_redis(data, address_of_the_cab)
        self.redis_dao.set_request_id(request_id)
        return request_id

    def _get_price_coefficient_from_request_threshold(self, request_id: str) -> Union[None, dict]:
        number_of_requests_in_cab_location: int = self.redis_dao.get_number_of_cabs_in_specific_origin(request_id)
        threshold_coefficient_query_set = ThresholdWeightModel.objects.filter(
            requests_threshold__lte=number_of_requests_in_cab_location).order_by('-requests_threshold').values()[:1]
        if threshold_coefficient_query_set:
            threshold_coefficient_record_dict: dict = threshold_coefficient_query_set.get()
            serialized_threshold_coefficient_record: CabPriceCoefficientSerializer = \
                CabPriceCoefficientSerializer(threshold_coefficient_record_dict)
            return serialized_threshold_coefficient_record
