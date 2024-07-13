# backend/services/day_point_service.py
from django.db.models import Exists, OuterRef
from django.db.models.functions import ExtractYear, ExtractMonth
from backend.models import DayPoint, RoomUtilization

class DayPointService:
    @staticmethod
    def get_unique_month_years():
        # Subquery to check if there is any utilization data for the month-year
        utilization_exists = RoomUtilization.objects.filter(
            day__date__year=ExtractYear(OuterRef('date')),
            day__date__month=ExtractMonth(OuterRef('date'))
        )

        unique_month_years = DayPoint.objects.annotate(
            year=ExtractYear('date'),
            month=ExtractMonth('date'),
            has_data=Exists(utilization_exists)
        ).values('year', 'month', 'has_data').distinct()

        # Convert to a list of dictionaries with "YYYY-MM" and "has_data"
        month_year_list = [
            {
                "month_year": f"{item['year']}-{str(item['month']).zfill(2)}",
                "has_data": item['has_data']
            }
            for item in unique_month_years
        ]

        return month_year_list