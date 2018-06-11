"""reservations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room_reservations.views import (
    Index,
    AddRoom,
    rooms,
    EditRoom,
    DeleteRoom,
    RoomReservation,
    DeleteReservation,
    Search,
    EditReservation
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('room', rooms, name="rooms-list"),
    path('room/add', AddRoom.as_view(), name="add-room"),
    path('room/edit/<room_id>', EditRoom.as_view(), name="edit-room"),
    path('room/delete/<room_id>', DeleteRoom.as_view(), name='delete-room'),
    path('reservation/<room_id>', RoomReservation.as_view(), name='reservation'),
    path('reservation/<room_id>/delete/<reservation_id>', DeleteReservation.as_view(), name="delete-reservation"),
    path('room/search', Search.as_view(), name='search'),
    path('reservation/<room_id>/<reservation_id>', EditReservation.as_view(), name="edit-reservation"),
]