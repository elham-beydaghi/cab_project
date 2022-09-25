from .models import PriceWeightModel
from .serializers import PriceWeightSerializer
from redis_db.redis_db import set_request_id, get_number_of_cabs_in_specific_origin

import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim
import json
import re
import datetime


class RequestThresholdRate(APIView):
    def post(self, request):
        data = json.loads(request.POST['data'])
        geolocator = Nominatim(user_agent="snapp_cab_app")
        address_of_the_cab = geolocator.reverse((data['lat'], data['lon']), language='en',
                                                exactly_one=True).raw['address']
        if address_of_the_cab:
            request_key = self._create_request_key_to_store_in_redis(data, address_of_the_cab)
            set_request_id(request_key=request_key)

        return address_of_the_cab

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


class PriceWeightViewSet(viewsets.ViewSet):
    query_set = PriceWeightModel.objects.all()
    serializer_class = PriceWeightSerializer

    def list(self, request):
        serialized_data = PriceWeightSerializer(instance=self.query_set, many=True)
        return Response(data=serialized_data.data)

    def retrieve(self, request, pk=None):
        data_object = get_object_or_404(self.query_set, pk=pk)
        serialized_data = PriceWeightSerializer(instance=data_object)
        return Response(data=serialized_data.data)

    def partial_update(self, request, pk=None):
        data_object = get_object_or_404(self.query_set, pk=pk)
        serialized_data = PriceWeightSerializer(instance=data_object, data=request.POST, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        return Response(data=serialized_data.errors)

    def destroy(self, request, pk=None):
        data_object = get_object_or_404(self.query_set, pk=pk)
        data_object.is_active = False
        data_object.save()
        return Response({'message': 'request threshold and price coefficient deleted'})
