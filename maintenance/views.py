from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Maintenance_Model
from .serializers import Maintenance_Serializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class MaintenanceViews(APIView):
    token_parameter = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Bearer <your_token>",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        manual_parameters=[token_parameter],
        responses={200: 'Maintenance get request successful'}
    )
    def get(self, request, id=""):
        if id:
            maintenance = Maintenance_Model.objects.filter(pk__icontains=id)
        else:
            maintenance = Maintenance_Model.objects.all()
        serializer = Maintenance_Serializer(maintenance, many=True)
        return Response({"message": "Maintenance get request successful", "data": serializer.data}, status=status.HTTP_200_OK)
    

    @swagger_auto_schema(
        request_body=Maintenance_Serializer,
        manual_parameters=[token_parameter],
        responses={201: 'Maintenance post request successful', 400: 'Invalid data'}
    )
    def post(self, request):
        copy_dict_of_data = request.data.copy()
        serializer = Maintenance_Serializer(data=copy_dict_of_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Maintenance Post Request Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=Maintenance_Serializer,
        manual_parameters=[token_parameter],
        responses={200: 'Maintenance updated successfully', 404: 'Data does not exist', 400: 'Invalid data'}
    )
    def put(self, request, id):
        try:
            maintenance = Maintenance_Model.objects.get(pk=id)
        except Maintenance_Model.DoesNotExist:
            return Response({"message": "Data does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Maintenance_Serializer(maintenance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Maintenance updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        manual_parameters=[token_parameter],
        responses={204: 'Maintenance data deleted successfully', 404: 'Data does not exist'}
    )
    def delete(self, request, id):
        try:
            maintenance = Maintenance_Model.objects.get(pk=id)
        except Maintenance_Model.DoesNotExist:
            return Response({"message": "Data does not exist"}, status=status.HTTP_404_NOT_FOUND)
        maintenance.delete()
        return Response({"message": "Maintenance data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
