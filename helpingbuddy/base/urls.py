from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:s>/', views.room, name = 'room'),
    path('create-room/', views.createRoom, name= 'create-room')
]
