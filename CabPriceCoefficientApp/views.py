from redis_db import RedisDataBaseAccessObject
from ThresholdWeightApp.models import ThresholdWeightModel
from ThresholdWeightApp.serializers import ThresholdWeightSerializer

from rest_framework.views import APIView

import hashlib
from geopy.geocoders import Nominatim
import json
import re
import datetime


class CabPriceCoefficientView(APIView):

    def __int__(self):
        self.redis_dao = RedisDataBaseAccessObject()

    def post(self, request):
        data = json.loads(request.POST['data'])
        geolocator = Nominatim(user_agent="snapp_cab_app")
        address_of_the_cab = geolocator.reverse((data['lat'], data['lon']), language='en',
                                                exactly_one=True).raw['address']
        if address_of_the_cab:
            request_id = self._set_request_id_in_redis(data, address_of_the_cab)
            price_coefficient = self._get_price_coefficient_from_request_threshold(request_id)
        return price_coefficient

    @staticmethod
    def _create_request_key_to_store_in_redis(data, address_of_the_cab):
        data_string = str(data)
        data_byte = data_string.encode('utf_8')
        data_hash = hashlib.md5(data_byte)

        now = datetime.datetime.now()
        date_time_now = now.strftime("%Y-%m-%d %H:%M:%S")

        suburb_of_cab_location = address_of_the_cab.get("suburb")
        cab_origin_number = re.findall(r'\d+', suburb_of_cab_location)[0]

        return '{}:{}:{}'.format(cab_origin_number, data_hash, date_time_now)

    def _set_request_id_in_redis(self, data, address_of_the_cab):
        request_id = self._create_request_key_to_store_in_redis(data, address_of_the_cab)
        self.redis_dao.set_request_id(request_id=request_id)
        return request_id

    def _get_price_coefficient_from_request_threshold(self, request_id):
        number_of_requests_in_cab_location = self.redis_dao.get_number_of_cabs_in_specific_origin(request_id)
        threshold_coefficient_record = ThresholdWeightModel.objects.filter(
            requests_threshold__lte=number_of_requests_in_cab_location).order_by('requests_threshold').values()[:1]
        serialized_data = ThresholdWeightSerializer(threshold_coefficient_record)
        return serialized_data['price_coefficient']
