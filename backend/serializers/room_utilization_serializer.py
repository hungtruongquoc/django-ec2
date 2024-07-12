# backend/serializers.py
from rest_framework import serializers
from backend.models import RoomUtilization


class RoomUtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomUtilization
        fields = '__all__'
