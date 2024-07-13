# backend/services/day_point_service.py
from django.db.models import F
from django.db.models.functions import ExtractYear, ExtractMonth
from backend.models import DayPoint


class DayPointService:
    @staticmethod
    def get_unique_month_years():
        unique_month_years = DayPoint.objects.annotate(
            year=ExtractYear('date'),
            month=ExtractMonth('date')
        ).values('year', 'month').distinct()

        # Convert to a list of "YYYY-MM" strings
        month_year_list = [
            f"{item['year']}-{str(item['month']).zfill(2)}" for item in unique_month_years
        ]

        return month_year_list
