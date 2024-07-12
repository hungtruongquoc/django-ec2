# backend/models/day_point.py
from django.db import models


class DayPoint(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.isoformat()
