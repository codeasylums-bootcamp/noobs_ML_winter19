from django.contrib import admin


# app level imports here
from . models import FlightData

# Register your models here.
admin.site.register(FlightData)