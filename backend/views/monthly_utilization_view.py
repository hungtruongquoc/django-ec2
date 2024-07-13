# backend/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.services import RoomUtilizationService


class MonthlyUtilizationView(APIView):

    def get(self, request):
        try:
            data = RoomUtilizationService.get_average_utilization_per_month()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
