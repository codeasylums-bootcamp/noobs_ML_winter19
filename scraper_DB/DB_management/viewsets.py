from rest_framework import viewsets

from . import models,serializers

class FlightDataViewSet(viewsets.ModelViewSet):
    queryset = models.FlightData.objects.all()
    serializer_class = serializers.FlightDataSerializer