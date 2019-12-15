from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # path('', views.home, name = "DBmgmt-home"),
    # path('about',views.about, name = "DBmgmt-about"),
    # # path('FlightData/',views.FlightDataView.as_view()),
    # path('flight_data',views.about, name = "post_flightdata"),
    # path('update_flight_data',views.about, name = "update_flightdata"),
    # path('cheap_flights',views.about, name = "cheap_flights"),
    # path('/<int:pk>/delete_flight_data',views.about, name = "delete_flight_data"),
]