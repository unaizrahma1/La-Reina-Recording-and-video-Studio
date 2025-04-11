from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/add/', views.add_artist, name='add_artist'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/update/<int:id>/', views.update_artist, name='update_artist'),
    path('artists/delete/<int:id>/', views.delete_artist, name='delete_artist'),
    path('add-booking/', views.add_booking, name='add_booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/update/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]