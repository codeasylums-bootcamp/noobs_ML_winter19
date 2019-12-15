from django.shortcuts import render
# from datetime import timedelta 

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from DB_management.serializers import FlightDataSerializer
from DB_management.models import FlightData

# flights = [
#     {
#         "name" : "air india",
#         "flight_number" :"1234",
#         "tod" : "1530",
#     },
#     {
#         "name" :"indigo",
#         "flight_number" : "1324",
#         "tod" : "1100",
#     },
#         {
#         "name" : "air india",
#         "flight_number" :"1234",
#         "tod" : "1530",
#     },
#     {
#         "name" :"indigo",
#         "flight_number" : "1324",
#         "tod" : "1100",
#     } ,   {
#         "name" : "air india",
#         "flight_number" :"1234",
#         "tod" : "1530",
#     },
#     { 
#         "name" :"indigo",
#         "flight_number" : "1324",
#         "tod" : "1100"
#     },
# ]
def home(request):
    
    return render(request,'DB_management/home.htm')

def about(request):
    context = {
        "flights" : FlightData.objects.all()
    }
    return render(request,'DB_management/about.htm',context)



# class FlightDataView(viewsets.ModelViewSet):
#     queryset = FlightData.objects.all()
#     serializer_class = FlightData

#     @action(methods=['POST'], detail=False, url_path="post_flightdata")
#     def post_flight_data(self, request):
#         serializer = FlightDataSerializer(data=request.data)
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             FlightData.objects.create(
#                 flight_name=validated_data['flight_name'],
#                 flight_st_date=validated_data['flight_st_date'],
#                 flight_end_date=validated_data['flight_end_date'],
#                 flight_st_time=validated_data['flight_st_time'],
#                 flight_end_time=validated_data['flight_end_time'],
#                 flight_price=validated_data['flight_price'],
#                 # flight_status = validated_data['flight_status'],

#             )
#             return HttpResponse(validated_data, status=status.HTTP_201_CREATED)
#         else:
#             return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @action(methods=['PUT'], detail=True, url_path="update_flightdata")
#     def update_flight_data(self, request, *args, **kwargs):
#         filter_kwargs = {self.lookup_field : self.kwargs[self.lookup_field]}
#         serializer = FlightDataSerializer(data=request.data)
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             To_update = FlightData.objects.get(**filter_kwargs)
#             To_update.flight_price = validated_data['flight_price']
#             # To_update.flight_status = validated_data['flight_status']
#             To_update.save()
#             return Response(validated_data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     @action(methods=['GET', 'POST'], detail=False, url_path="cheap_flights")
#     def cheap_flights(self, request):
#         cheap_flights = FlightData.objects.filter(flight_price__lte=5000)
#         serializer = FlightDataSerializer(cheap_flights, many=True)
#         if serializer.is_valid():
#             context = {
#                 "flights": serializer.validated_data
#             }
#             return render(request,'DB_management/about',context)
#             # return Response(serializer.data, status.HTTP_200_OK)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     @action(methods=['DELETE'],detail=True, url_path="delete_flight_data")
#     def delete_flight_data(self, request,pk):
#         delete_flight = FlightData.objects.filter(id = pk)
#         # filter_kwargs = {self.lookup_field : self.kwargs[self.lookup_field]}
#         serializer = FlightDataSerializer(data = request.data)
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             To_Delete = serializer.validated_data
#             To_Delete.delete()
#             context ={
#                 "flights":validated_data
#             }
#             return render(request,'DB_management/about.htm',context)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
