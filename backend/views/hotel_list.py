from rest_framework import generics
from backend.models import Hotel
from backend.serializers import HotelSerializer


class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
