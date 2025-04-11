from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/add/', views.add_artist, name='add_artist'),
    path('artists/', views.artist_list, name='artist_list'),
]