from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle_Model
from .serializers import Vehicle_Serializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class VehicleViews(APIView):
    token_parameter = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Bearer <your_token>",
        type=openapi.TYPE_STRING,
    )
        
    @swagger_auto_schema(
        manual_parameters=[
            token_parameter,
            openapi.Parameter('make', openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Filter by vehicle make"),
            openapi.Parameter('price', openapi.IN_QUERY, type=openapi.TYPE_NUMBER, description="Filter by maximum price"),
            openapi.Parameter('range', openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Filter by price range (e.g. '10000-20000')"),
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="Filter by vehicle year"),
        ]
    )
    def get(self, request):
        make = request.GET.get('make')
        price = request.GET.get('price')
        v_range = request.GET.get('range')
        year = request.GET.get('year')

        vehicle = Vehicle_Model.objects.filter(user=request.user)

        if make:
            vehicle = vehicle.filter(make__iexact=make)
        if price:
            vehicle = vehicle.filter(price__lte=float(price))
        if v_range:
            min_price, max_price = map(float, v_range.split('-'))
            vehicle = vehicle.filter(price__gte=min_price, price__lte=max_price)
        if year:
            vehicle = vehicle.filter(year__iexact=year)

        serializer = Vehicle_Serializer(vehicle, many=True)
        return Response({"message": "Vehicle get request successful", "data": serializer.data}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=Vehicle_Serializer, manual_parameters=[token_parameter])
    def post(self, request):
        copy_dict_of_data = request.data.copy() 
        copy_dict_of_data['user'] = request.user.id 
        
        serializer = Vehicle_Serializer(data=copy_dict_of_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vehicle Post Request Successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=Vehicle_Serializer, manual_parameters=[token_parameter])
    def put(self, request, id):
        try:
            vehicle = Vehicle_Model.objects.get(pk=id)
        except Vehicle_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = Vehicle_Serializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vehicles updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={204: 'Vehicles data deleted successfully'}, manual_parameters=[token_parameter])
    def delete(self, request, id):
        try:
            vehicles = Vehicle_Model.objects.get(pk=id)
        except Vehicle_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        vehicles.delete()
        return Response({"message": "Vehicles data deleted successfully"},status=status.HTTP_204_NO_CONTENT)