# backend/serializers.py
from rest_framework import serializers


class MonthYearSerializer(serializers.Serializer):
    month_year = serializers.CharField()
