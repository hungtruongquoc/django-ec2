# backend/serializers.py
from rest_framework import serializers
from backend.models import Hotel
from .room_serializer import RoomSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    rooms = RoomSerializer(many=True, read_only=True)
