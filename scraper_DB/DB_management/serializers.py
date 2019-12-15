from rest_framework import serializers


from DB_management.models import FlightData



class FlightDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightData
        fields = ['flight_st_date','flight_end_date','flight_st_time','flight_end_time','flight_price']
    


    # flight_name = serializers.CharField(required=True)
    # flight_st_date = serializers.DateField(required=True)
    # flight_end_date = serializers.DateField(required=True)
    # flight_st_time = serializers.TimeField(required=True)
    # flight_end_time = serializers.TimeField(required=True)
    # flight_price = serializers.IntegerField(required=True)

    # def validate(self, data):
    #     flight_name = data.get('flight_name', None)
    #     flight_st_date = data.get('flight_st_date', None)
    #     flight_end_date = data.get('flight_end_date', None)
    #     flight_st_time = data.get('flight_st_time', None)
    #     flight_end_time = data.get('flight_end_time',None)
    #     flight_price = data.get('flight_price', None)
    #     # flight_status = data.get('flight_status', None)

    #     return {
    #         "flight_name": flight_name, "flight_st_date": flight_st_date,
    #         "flight_end_date": flight_end_date, "flight_st_time": flight_st_time,
    #         "flight_end_time": flight_end_time, "flight_price": flight_price,
    #         # "flight_status": flight_status,
    #     }

