# backend/views.py
from rest_framework import generics
from backend.models import RoomUtilization
from backend.serializers import RoomUtilizationSerializer


class RoomUtilizationList(generics.ListCreateAPIView):
    queryset = RoomUtilization.objects.all()
    serializer_class = RoomUtilizationSerializer
