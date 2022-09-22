from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PriceWeightModel
from .serializers import PriceWeightSerializer
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


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