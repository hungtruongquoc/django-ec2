# backend/models/room_utilization.py
from django.db import models
from .room import Room
from .day_point import DayPoint


class RoomUtilization(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.ForeignKey(DayPoint, on_delete=models.CASCADE)
    utilization = models.FloatField()  # Utilization as a percentage (0.0 to 1.0)

    class Meta:
        unique_together = ('room', 'day')

    def __str__(self):
        return f"Room {self.room.id} on {self.day.date}: {self.utilization * 100:.2f}%"
