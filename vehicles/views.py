from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle_Model
from .serializers import Vehicle_Serializer
from rest_framework import status



class VehicleViews(APIView):
    def get(self, request):
        vehicle = Vehicle_Model.objects.all()
        serializer = Vehicle_Serializer(vehicle, many=True)
        return Response({"message": "Vehicle Get request succesful", "data": serializer.data }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Vehicle_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vehicle Post Request Successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            vehicle = Vehicle_Model.objects.get(pk=id)
        except Vehicle_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = Vehicle_Serializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vehicles deleted successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            vehicles = Vehicle_Model.objects.get(pk=id)
        except Vehicle_Model.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        vehicles.delete()
        return Response({"message": "Data deleted successfully"},status=status.HTTP_204_NO_CONTENT)