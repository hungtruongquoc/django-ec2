# backend/management/commands/seed.py
import random
from django.core.management.base import BaseCommand

from backend.models import DayPoint, RoomUtilization
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
        self._seed_room_utilization()
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

    def _seed_room_utilization(self):
        rooms = Room.objects.all()
        start_date = date(2024, 1, 1)
        end_date = date(2024, 2, 29)
        delta = timedelta(days=1)

        current_date = start_date
        while current_date <= end_date:
            for room in rooms:
                day_point = DayPoint.objects.get(date=current_date)

                # Different utilization patterns for different hotels
                if room.hotel.code == 'H1':
                    utilization_value = random.uniform(0.0, 0.5)  # Lower utilization
                elif room.hotel.code == 'H2':
                    utilization_value = random.uniform(0.5, 1.0)  # Higher utilization
                else:
                    utilization_value = random.uniform(0.25, 0.75)  # Mid-range utilization

                utilization_data = {
                    'room': room,
                    'day': day_point,
                    'utilization': utilization_value,
                }
                utilization, created = RoomUtilization.objects.update_or_create(
                    room=room,
                    day=day_point,
                    defaults={'utilization': utilization_data['utilization']}
                )
                if created:
                    self.stdout.write(
                        f'Created RoomUtilization for {room.name} on {current_date}: {utilization.utilization * 100:.2f}%')
                else:
                    self.stdout.write(
                        f'Updated RoomUtilization for {room.name} on {current_date}: {utilization.utilization * 100:.2f}%')
            current_date += delta
