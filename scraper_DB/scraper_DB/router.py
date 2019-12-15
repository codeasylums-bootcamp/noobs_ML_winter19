from DB_management.viewsets import FlightDataViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('flightdata',FlightDataViewSet)