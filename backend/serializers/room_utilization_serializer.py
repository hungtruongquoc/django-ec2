# backend/serializers.py
from rest_framework import serializers
from backend.models import RoomUtilization
from backend.models import Room
from decimal import Decimal


class RoomUtilizationSerializer(serializers.ModelSerializer):
    utilization = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = RoomUtilization
        fields = '__all__'

    def validate_utilization(self, value):
        if not isinstance(value, Decimal):
            raise serializers.ValidationError("Utilization must be a decimal number.")
        if not (Decimal('0.00') <= value <= Decimal('1.00')):
            raise serializers.ValidationError("Utilization must be between 0 and 1.")
        return value

    def validate_room(self, value):
        if not Room.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Room must exist in the database.")
        return value
