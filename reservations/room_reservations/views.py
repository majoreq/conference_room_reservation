from django.shortcuts import render, redirect
from django.views import View
from .models import Room, Reservation
from django.http import HttpResponse
import datetime

class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class AddRoom(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, requset):
        name = requset.POST.get('name')
        capacity = requset.POST.get('capacity')
        projector = requset.POST.get('projector')
        new_room = Room()
        new_room.name = name
        new_room.capacity = capacity
        new_room.projector = projector
        new_room.save()
        return redirect('rooms-list')


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms':rooms})


class DeleteRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()
        return redirect('rooms-list')


class DeleteReservation(View):
    def get(self, request,room_id, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        reservation.delete()
        reservations = Reservation.objects.all()
        room = Room.objects.get(id=room_id)
        return redirect('/reservation/{}'.format(room.id))


class EditRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, 'edit_room.html', {'room':room})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')
        room.name=name
        room.capacity=capacity
        room.projector=projector
        room.save()
        return redirect('rooms-list')


class RoomReservation(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        reservations = Reservation.objects.filter(room=room).order_by('date')
        return render(request, 'reservation.html', {'room':room, 'reservations':reservations})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        date = request.POST.get('date')
        comment = request.POST.get('comment')
        taken_date = Reservation.objects.filter(room=room, date=date)
        current_date = datetime.datetime.today()
        formated_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        datetime.date(formated_date.year, formated_date. month, formated_date.day)
        if current_date > formated_date:
            return HttpResponse("data z przeszłości")
        if taken_date:
            return HttpResponse("Zajęte")
        new_reservation = Reservation()
        new_reservation.date = date
        new_reservation.comment = comment
        new_reservation.room = room
        new_reservation.save()
        reservations = Reservation.objects.filter(room=room)
        return render(request, 'reservation.html', {'room': room, 'reservations': reservations})


class EditReservation(View):
    def get(self, request,room_id, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        print(reservation.comment)
        print(reservation.date)
        return render(request, 'edit_reservation.html', {'reservation': reservation})

    def post(self, request, room_id, reservation_id):
        room = Room.objects.get(id=room_id)
        date = request.POST.get('date')
        comment = request.POST.get('comment')
        taken_date = Reservation.objects.filter(room=room, date=date)
        current_date = datetime.datetime.today()
        formated_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        datetime.date(formated_date.year, formated_date.month, formated_date.day)
        if current_date > formated_date:
            return HttpResponse("data z przeszłości")
        if taken_date:
            return HttpResponse("Zajęte")
        edited_reservation = Reservation.objects.get(id=reservation_id)
        edited_reservation.date = date
        edited_reservation.comment = comment
        edited_reservation.room = room
        edited_reservation.save()
        reservations = Reservation.objects.filter(room=room)
        return render(request, 'reservation.html', {'room': room, 'reservations': reservations})


class Search(View):
    def get(self, request):
        name = request.GET.get('name')
        capacity = request.GET.get('capacity')
        date = request.GET.get('date')
        projector = request.GET.get('projector')
        rooms = Room.objects.all()
        if name:
            rooms = rooms.filter(name__contains=name)
        if projector:
            rooms = rooms.filter(projector=projector)
        if capacity:
            rooms = rooms.filter(capacity__gte=capacity)
        if date:
            rooms = rooms.exclude(reservation__date=date)
        return render(request,'search.html',{'rooms':rooms})