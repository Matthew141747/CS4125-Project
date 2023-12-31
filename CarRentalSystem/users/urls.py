from django.urls import path
from . import views

#Note, I'm pretty sure this class is not needed

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reservations/', views.ReservationView.as_view(), name='reservations'),
    path('load-car-models/', views.load_car_model, name='load_car_models'),
    path('inventory/', views.add_vehicle, name='inventory'),
]