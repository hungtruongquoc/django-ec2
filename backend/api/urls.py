from django.urls import path
from backend.views import RoomUtilizationList, HotelList, MonthlyUtilizationView

urlpatterns = [
    path('room-utilization/', RoomUtilizationList.as_view(), name='room-utilization-list'),
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('room-utilization/monthly/', MonthlyUtilizationView.as_view(), name='monthly-utilization'),
    path('room-utilization/monthly/<str:month>/', MonthlyUtilizationView.as_view(),
         name='monthly-utilization-specific'),
]
