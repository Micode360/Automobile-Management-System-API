from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sales_Model
from .serializers import Sales_Serializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SalesViews(APIView):
    token_parameter = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Bearer <your_token>",
        type=openapi.TYPE_STRING,
    )
        
    @swagger_auto_schema(
        manual_parameters=[token_parameter],
        responses={200: 'Sales get request successful'}
    )
    def get(self, request, id=""):
        sales = Sales_Model.objects.filter(pk__icontains=id)
        serializer = Sales_Serializer(sales, many=True)
        return Response({"message": "Sales get request successful", "data": serializer.data }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=Sales_Serializer,
        manual_parameters=[token_parameter],
        responses={200: 'Sales post request successful', 400: 'Invalid data'}
    )
    def post(self, request):
        copy_dict_of_data = request.data.copy()
        copy_dict_of_data['buyer'] = request.user.id or None # None is added if i want to make someone who is not authenticated to buy a vehicle
        
        serializer = Sales_Serializer(data=copy_dict_of_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sales post Request Successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=Sales_Serializer,
        manual_parameters=[token_parameter],
        responses={200: 'Sales record updated successfully', 404: 'Data does not exist', 400: 'Invalid data'}
    )
    def put(self, request, id):
        try:
            sales = Sales_Model.objects.get(pk=id)
        except sales.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = Sales_Serializer(sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sales Record is updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        manual_parameters=[token_parameter],
        responses={204: 'Sales record deleted successfully', 404: 'Data does not exist'}
    )
    def delete(self, request, id):
        try:
            sales = Sales_Model.objects.get(pk=id)
        except Sales_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        sales.delete()
        return Response({"message": "Sales record deleted successfully"},status=status.HTTP_204_NO_CONTENT)