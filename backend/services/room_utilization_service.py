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
    def get_utilization_by_day(month):
        try:
            # Parse the month parameter
            month_date = datetime.strptime(month, "%Y-%m")

            # Filter RoomUtilization objects by the given month
            utilization_data = RoomUtilization.objects.filter(
                day__date__year=month_date.year,
                day__date__month=month_date.month
            ).values(
                'day__date', 'room__hotel__name', 'room__name', 'utilization'
            )

            # Prepare the response data
            daily_data = {}
            for item in utilization_data:
                day_str = item['day__date'].strftime("%Y-%m-%d")
                if day_str not in daily_data:
                    daily_data[day_str] = {
                        "date": day_str,
                        "hotels": {}
                    }
                hotel_name = item['room__hotel__name']
                if hotel_name not in daily_data[day_str]["hotels"]:
                    daily_data[day_str]["hotels"][hotel_name] = {
                        "hotel": hotel_name,
                        "rooms": []
                    }
                room_data = {
                    "room": item['room__name'],
                    "utilization": item['utilization']
                }
                daily_data[day_str]["hotels"][hotel_name]["rooms"].append(room_data)

            # Convert nested dictionaries to lists
            result = {
                "month": month,
                "days": [
                    {
                        "date": day,
                        "hotels": list(day_data["hotels"].values())
                    }
                    for day, day_data in daily_data.items()
                ]
            }

            return result
        except ValueError:
            raise ValueError("Invalid month format. Use YYYY-MM.")
