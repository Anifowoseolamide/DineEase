from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.ReservationCreateView.as_view(), name='reservation_form'),
    path('success/', views.reservation_success, name='reservation_success'),
]
