# backend/management/commands/seed.py
import random
from django.core.management.base import BaseCommand

from backend.models import DayPoint
from backend.models import Hotel
from backend.models import Room
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Seed the database with initial data for Hotel and Room'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        self._seed_hotels()
        self._seed_rooms()
        self._seed_day_points()
        self.stdout.write('Data seeded successfully!')

    def _seed_hotels(self):
        hotels = [
            {'name': 'Hotel One', 'code': 'H1', 'address': '123 Main St'},
            {'name': 'Hotel Two', 'code': 'H2', 'address': '456 Elm St'},
            {'name': 'Hotel Three', 'code': 'H3', 'address': '789 Oak St'},
        ]

        for hotel_data in hotels:
            hotel, created = Hotel.objects.get_or_create(**hotel_data)
            if created:
                self.stdout.write(f'Created hotel: {hotel.name}')
            else:
                self.stdout.write(f'Hotel already exists: {hotel.name}')

    def _seed_rooms(self):
        hotels = Hotel.objects.all()

        for hotel in hotels:
            for i in range(1, 11):  # Create 10 rooms for each hotel
                room_data = {
                    'name': f'Room {i}',
                    'code': f'R{i}',
                    'hotel': hotel
                }
                room, created = Room.objects.get_or_create(**room_data)
                if created:
                    self.stdout.write(f'Created room: {room.name} in {hotel.name}')
                else:
                    self.stdout.write(f'Room already exists: {room.name} in {hotel.name}')

    def _seed_day_points(self):
        start_date = date(2024, 1, 1)
        end_date = date(2024, 12, 31)
        delta = timedelta(days=1)

        current_date = start_date
        while current_date <= end_date:
            day_point, created = DayPoint.objects.get_or_create(date=current_date)
            if created:
                self.stdout.write(f'Created DayPoint: {day_point.date}')
            else:
                self.stdout.write(f'DayPoint already exists: {day_point.date}')
            current_date += delta
