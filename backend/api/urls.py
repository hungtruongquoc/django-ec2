from django.urls import path
from backend.views import RoomUtilizationList, HotelList, MonthlyUtilizationView, DailyUtilizationByHotelsView, \
    MonthYearListView

urlpatterns = [
    path('room-utilization/', RoomUtilizationList.as_view(), name='room-utilization-list'),
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('room-utilization/average-per-month/', MonthlyUtilizationView.as_view(),
         name='average-utilization-per-month'),
    path('room-utilization/max-daily-by-hotels/<str:month>/', DailyUtilizationByHotelsView.as_view(),
         name='max-daily-utilization-by-all-hotels'),
    path('month-years/', MonthYearListView.as_view(), name='month-year-list'),
]
