# backend/services/utilization_service.py
from django.db.models import Avg
from backend.models import RoomUtilization
from datetime import datetime


class RoomUtilizationService:
    @staticmethod
    def get_average_utilization_per_month():
        # Get all RoomUtilization records and calculate the average utilization per month
        utilization_data = RoomUtilization.objects.values('day__date__year', 'day__date__month').annotate(
            avg_utilization=Avg('utilization'))

        # Prepare the response data
        monthly_data = []
        for item in utilization_data:
            month_str = f"{item['day__date__year']}-{item['day__date__month']:02}"
            monthly_data.append({
                "month": month_str,
                "avg_utilization": item['avg_utilization']
            })
        return monthly_data

    @staticmethod
    def get_monthly_utilization_by_hotels(month=None):
        try:
            # Parse the month parameter
            month_date = datetime.strptime(month, "%Y-%m")

            # Filter RoomUtilization objects by the given month
            utilization_data = RoomUtilization.objects.filter(
                day__date__year=month_date.year,
                day__date__month=month_date.month
            ).values(
                'day__date', 'room__hotel__name', 'utilization'
            )

            # Prepare the response data
            daily_data = {}
            for item in utilization_data:
                day_str = item['day__date'].strftime("%Y-%m-%d")
                if day_str not in daily_data:
                    daily_data[day_str] = {
                        "date": day_str,
                        "hotels": []
                    }
                hotel_data = {
                    "hotel": item['room__hotel__name'],
                    "utilization": item['utilization']
                }
                daily_data[day_str]["hotels"].append(hotel_data)

            # Convert the daily data dictionary to a list of daily data
            result = {
                "month": month,
                "days": list(daily_data.values())
            }

            return result
        except ValueError:
            raise ValueError("Invalid month format. Use YYYY-MM.")
