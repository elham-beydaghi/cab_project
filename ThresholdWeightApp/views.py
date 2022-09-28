from ThresholdWeightApp.models import ThresholdWeightModel
from ThresholdWeightApp.serializers import ThresholdWeightSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ThresholdWeightListView(APIView):

    def get(self, request):
        thresholds_weights = ThresholdWeightModel.objects.all()
        serialized_thresholds_weights = ThresholdWeightSerializer(instance=thresholds_weights, many=True)
        return Response(serialized_thresholds_weights.data, status=status.HTTP_200_OK)


class ThresholdWeightCreateView(APIView):
    def post(self, request):
        serialized_threshold_weight = ThresholdWeightSerializer(data=request.data)
        if serialized_threshold_weight.is_valid():
            serialized_threshold_weight.save()
            return Response(serialized_threshold_weight.data, status=status.HTTP_201_CREATED)
        return Response(serialized_threshold_weight.errors, status=status.HTTP_400_BAD_REQUEST)


class ThresholdWeightUpdateView(APIView):
    def put(self, request, pk=None):
        threshold_weight = ThresholdWeightModel.objects.get(pk=pk)
        serialized_threshold_weight = ThresholdWeightSerializer(instance=threshold_weight, data=request.data)
        if serialized_threshold_weight.is_valid():
            serialized_threshold_weight.save()
            return Response(serialized_threshold_weight.data, status=status.HTTP_200_OK)
        return Response(serialized_threshold_weight.errors, status=status.HTTP_400_BAD_REQUEST)


class ThresholdWeightDeleteView(APIView):
    def delete(self, request, pk=None):
        threshold_weight = ThresholdWeightModel.objects.get(pk=pk)
        threshold_weight.delete()
        return Response({'message': 'request threshold and price coefficient deleted'}, status=status.HTTP_200_OK)
