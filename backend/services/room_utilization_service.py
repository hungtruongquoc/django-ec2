# backend/services/utilization_service.py
from django.db.models import Avg
from backend.models import RoomUtilization


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
