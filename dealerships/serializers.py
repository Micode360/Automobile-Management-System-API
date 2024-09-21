from rest_framework import serializers
from .models import Dealership_Model
from users.models import CustomUser


class Dealership_Serializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    class Meta:
        model = Dealership_Model
        fields = '__all__'


    def validate(self, attrs):
        name = attrs.get('name')
        if len(name) < 4:
            raise serializers.ValidationError("Name must be more than 4 characters")
        return attrs
    
    def create(self, validated_data):
        return Dealership_Model.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance