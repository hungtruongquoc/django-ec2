# backend/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.services.day_point_service import DayPointService


class MonthYearListView(APIView):

    def get(self, request):
        try:
            month_years = DayPointService.get_unique_month_years()
            return Response(month_years, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
