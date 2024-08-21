from rest_framework import serializers
from .models import Vehicle_Model



class Vehicle_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Model
        fields = '__all__'


    def validate(self, attrs):
        make = attrs.get('make')
        if len(make) < 4:
            raise serializers.ValidationError("Name must be more than 4 characters")
        return attrs
    
    def create(self, validated_data):
        return Vehicle_Model.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.color = validated_data.get('color', instance.color)
        instance.vin = validated_data.get('vin', instance.vin)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance