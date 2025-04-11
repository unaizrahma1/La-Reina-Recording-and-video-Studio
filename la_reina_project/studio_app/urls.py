from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/add/', views.add_artist, name='add_artist'),
]