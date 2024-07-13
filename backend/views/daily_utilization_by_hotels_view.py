from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.services import RoomUtilizationService


class DailyUtilizationByHotelsView(APIView):

    def get(self, request, month=None):
        try:
            data = RoomUtilizationService.get_utilization_by_day(month)
            return Response(data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
