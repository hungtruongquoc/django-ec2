# backend/services/day_point_service.py
from django.db.models import Func, F

from backend.models import DayPoint


class DayPointService:
    @staticmethod
    def get_unique_month_years():
        unique_month_years = DayPoint.objects.annotate(
            year=Func(F('date'), function='YEAR'),
            month=Func(F('date'), function='MONTH')
        ).values('year', 'month').distinct()

        # Convert to a list of "YYYY-MM" strings
        month_year_list = [
            f"{item['year']}-{str(item['month']).zfill(2)}" for item in unique_month_years
        ]

        return month_year_list
