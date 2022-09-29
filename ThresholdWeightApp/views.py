from ThresholdWeightApp.models import ThresholdWeightModel
from ThresholdWeightApp.serializers import ThresholdWeightSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ThresholdWeightListView(APIView):

    def get(self, request) -> Response:
        thresholds_weights = ThresholdWeightModel.objects.all()
        serialized_thresholds_weights: ThresholdWeightSerializer = ThresholdWeightSerializer(
            instance=thresholds_weights, many=True)
        return Response(serialized_thresholds_weights.data, status=status.HTTP_200_OK)


class ThresholdWeightCreateView(APIView):
    def post(self, request) -> Response:
        serialized_threshold_weight: ThresholdWeightSerializer = ThresholdWeightSerializer(data=request.data)
        if serialized_threshold_weight.is_valid():
            serialized_threshold_weight.save()
            return Response(serialized_threshold_weight.data, status=status.HTTP_201_CREATED)
        return Response(serialized_threshold_weight.errors, status=status.HTTP_400_BAD_REQUEST)


class ThresholdWeightUpdateView(APIView):
    def put(self, request, pk: int = None) -> Response:
        threshold_weight = ThresholdWeightModel.objects.get(pk=pk)
        serialized_threshold_weight: ThresholdWeightSerializer = ThresholdWeightSerializer(instance=threshold_weight,
                                                                                           data=request.data,
                                                                                           partial=True)
        if serialized_threshold_weight.is_valid():
            serialized_threshold_weight.save()
            return Response(serialized_threshold_weight.data, status=status.HTTP_200_OK)
        return Response(serialized_threshold_weight.errors, status=status.HTTP_400_BAD_REQUEST)


class ThresholdWeightDeleteView(APIView):
    def delete(self, request, pk: int = None) -> Response:
        try:
            threshold_weight = ThresholdWeightModel.objects.get(pk=pk)
            threshold_weight.delete()
            return Response({'message': 'request threshold and price coefficient deleted'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message': 'request threshold doesnt exist'}, status=status.HTTP_404_NOT_FOUND)
