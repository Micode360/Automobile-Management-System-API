from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dealership_Model
from .serializers import Dealership_Serializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DealershipViews(APIView):
    token_parameter = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Bearer <your_token>",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        manual_parameters=[token_parameter],
        responses={200: 'Dealership get request successful'}
    )
    def get(self, request, id=""):
        dealership = Dealership_Model.objects.filter(pk__icontains=id)
        serializer = Dealership_Serializer(dealership, many=True)
        return Response({"message": "Dealership get request successful", "data": serializer.data }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=Dealership_Serializer,
        manual_parameters=[token_parameter],
        responses={200: 'Dealership post request successful', 400: 'Invalid data'}
    )
    def post(self, request):
        copy_dict_of_data = request.data.copy()
        copy_dict_of_data['user'] = request.user.id 
        
        serializer = Dealership_Serializer(data=copy_dict_of_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vehicle Post Request Successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=Dealership_Serializer,
        manual_parameters=[token_parameter],
        responses={200: 'Deal is updated successfully', 404: 'Data does not exist', 400: 'Invalid data'}
    )
    def put(self, request, id):
        try:
            dealership = Dealership_Model.objects.get(pk=id)
        except dealership.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = Dealership_Serializer(dealership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The deal is updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        manual_parameters=[token_parameter],
        responses={204: 'Dealership data deleted successfully', 404: 'Data does not exist'}
    )
    def delete(self, request, id):
        try:
            dealership = Dealership_Model.objects.get(pk=id)
        except Dealership_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        dealership.delete()
        return Response({"message": "Dealership data deleted successfully"},status=status.HTTP_204_NO_CONTENT)