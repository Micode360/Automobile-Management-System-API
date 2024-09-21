from rest_framework import serializers
from .models import Sales_Model
from users.models import CustomUser


class Sales_Serializer(serializers.ModelSerializer):
    buyer = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    class Meta:
        model = Sales_Model
        fields = '__all__'


    def validate(self, attrs):
        buyer_name = attrs.get('buyer_name')
        if len(buyer_name) < 4:
            raise serializers.ValidationError("Name must be more than 4 characters")
        return attrs
    
    def create(self, validated_data):
        return Sales_Model.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.buyer_name = validated_data.get('buyer_name', instance.buyer_name)
        instance.buyer_contact = validated_data.get('buyer_contact', instance.buyer_contact)
        instance.buyer_drivers_liscense = validated_data.get('buyer_drivers_liscense', instance.buyer_drivers_liscense)
        instance.vehicle_sold = validated_data.get('vehicle_sold', instance.vehicle_sold)
        instance.sale_price = validated_data.get('sale_price', instance.sale_price)
        instance.sale_date = validated_data.get('sale_date', instance.sale_date)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance