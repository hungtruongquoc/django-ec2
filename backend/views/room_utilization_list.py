# backend/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from backend.models import RoomUtilization
from backend.serializers import RoomUtilizationSerializer


class RoomUtilizationList(generics.ListCreateAPIView):
    queryset = RoomUtilization.objects.all()
    serializer_class = RoomUtilizationSerializer

    def perform_create(self, serializer):
        room = serializer.validated_data.get('room')
        day = serializer.validated_data.get('day')
        utilization = serializer.validated_data.get('utilization')

        # Check if the combination of room and day already exists
        instance, created = RoomUtilization.objects.update_or_create(
            room=room,
            day=day,
            defaults={'utilization': utilization}
        )
        return instance

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(RoomUtilizationSerializer(instance).data, status=status.HTTP_201_CREATED, headers=headers)
