from django.urls import path
from backend.views import RoomUtilizationList, HotelList

urlpatterns = [
    path('room-utilization/', RoomUtilizationList.as_view(), name='room-utilization-list'),
    path('hotels/', HotelList.as_view(), name='hotel-list'),
]