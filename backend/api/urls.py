from django.urls import path
from backend.views import RoomUtilizationList, HotelList, MonthlyUtilizationView, MonthlyUtilizationByHotelsView

urlpatterns = [
    path('room-utilization/', RoomUtilizationList.as_view(), name='room-utilization-list'),
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('room-utilization/average-per-month/', MonthlyUtilizationView.as_view(),
         name='average-utilization-per-month'),
    path('room-utilization/monthly-by-hotels/<str:month>/', MonthlyUtilizationByHotelsView.as_view(),
         name='daily-utilization-by-all-hotels'),
]
