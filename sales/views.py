from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sales_Model
from .serializers import Sales_Serializer
from rest_framework import status


class SalesViews(APIView):
    def get(self, request, id=""):
        sales = Sales_Model.objects.filter(pk__icontains=id)
        serializer = Sales_Serializer(sales, many=True)
        return Response({"message": "Sales get request successful", "data": serializer.data }, status=status.HTTP_200_OK)
    
    def post(self, request):
        copy_dict_of_data = request.data.copy()
        copy_dict_of_data['buyer'] = request.user.id or None # None is added if i want to make someone who is not authenticated to buy a vehicle
        
        serializer = Sales_Serializer(data=copy_dict_of_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sales post Request Successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
    def delete(self, request, id):
        try:
            sales = Sales_Model.objects.get(pk=id)
        except Sales_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        sales.delete()
        return Response({"message": "Sales record deleted successfully"},status=status.HTTP_204_NO_CONTENT)