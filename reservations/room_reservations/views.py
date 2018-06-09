from django.shortcuts import render, redirect
from django.views import View
from .models import Room, Reservation

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

