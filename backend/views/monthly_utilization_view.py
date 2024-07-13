# backend/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from backend.models import RoomUtilization
from datetime import datetime


class MonthlyUtilizationView(APIView):

    def get(self, request, month=None):
        if month:
            try:
                # Parse the month parameter
                month = datetime.strptime(month, "%Y-%m")

                # Filter RoomUtilization objects by the given month
                utilizations = RoomUtilization.objects.filter(day__date__year=month.year, day__date__month=month.month)

                # Calculate the average utilization for the month
                avg_utilization = utilizations.aggregate(Avg('utilization'))['utilization__avg']

                # Prepare the response data for the month
                data = {
                    "month": month.strftime("%Y-%m"),
                    "avg_utilization": avg_utilization if avg_utilization is not None else 0,
                    "hotels": []
                }

                # Calculate average utilization for each hotel in the month
                hotel_data = utilizations.values('room__hotel__name').annotate(avg_utilization=Avg('utilization'))
                for item in hotel_data:
                    data["hotels"].append({
                        "hotel": item['room__hotel__name'],
                        "avg_utilization": item['avg_utilization']
                    })

                return Response(data, status=status.HTTP_200_OK)

            except ValueError:
                return Response({"error": "Invalid month format. Use YYYY-MM."}, status=status.HTTP_400_BAD_REQUEST)

        else:
            # Get all months with utilization data
            utilizations = RoomUtilization.objects.all()

            # Calculate the average utilization for each month and each hotel
            utilization_data = utilizations.values('day__date__year', 'day__date__month', 'room__hotel__name').annotate(
                avg_utilization=Avg('utilization'))

            # Prepare the response data
            monthly_data = {}
            for item in utilization_data:
                month_str = f"{item['day__date__year']}-{item['day__date__month']:02}"
                if month_str not in monthly_data:
                    monthly_data[month_str] = {
                        "month": month_str,
                        "avg_utilization": 0,
                        "hotels": []
                    }

                hotel_data = {
                    "hotel": item['room__hotel__name'],
                    "avg_utilization": item['avg_utilization']
                }
                monthly_data[month_str]["hotels"].append(hotel_data)

            # Convert monthly_data to a list for the response
            data = list(monthly_data.values())
            return Response(data, status=status.HTTP_200_OK)