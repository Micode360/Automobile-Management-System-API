from rest_framework import serializers
from .models import Maintenance_Model
from vehicles.models import Vehicle_Model  

class Maintenance_Serializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle_Model.objects.all())
    
    class Meta:
        model = Maintenance_Model
        fields = '__all__'

    def validate(self, attrs):
        maintenance_type = attrs.get('maintenance_type')
        if len(maintenance_type) < 3:
            raise serializers.ValidationError("Maintenance type must be more than 3 characters")
        return attrs

    def create(self, validated_data):
        return Maintenance_Model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.vehicle = validated_data.get('vehicle', instance.vehicle)
        instance.maintenance_type = validated_data.get('maintenance_type', instance.maintenance_type)
        instance.maintenance_date = validated_data.get('maintenance_date', instance.maintenance_date)
        instance.service_provider = validated_data.get('service_provider', instance.service_provider)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
