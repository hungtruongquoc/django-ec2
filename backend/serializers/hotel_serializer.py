# backend/serializers.py
from rest_framework import serializers
from backend.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
