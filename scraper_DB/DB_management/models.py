from django.db import models
from django.utils import timezone

# Create your models here.


class FlightData(models.Model):
    flight_name = models.CharField(max_length=64)
    flight_st_date = models.DateField(default=timezone.now)
    flight_end_date = models.DateField(default=timezone.now)
    flight_st_time = models.TimeField(default=timezone.now)
    flight_end_time = models.TimeField(default=timezone.now)
    flight_price = models.IntegerField()
    # flight_status = models.CharField(max_length=64)
    
    def __str__(self):
        return str(self.flight_name)
    