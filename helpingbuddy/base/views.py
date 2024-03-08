from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id':1, 'name': 'Python Buddy'},
#     {'id':2, 'name': 'Java Buddy'},
#     {'id':3, 'name': 'Dart Buddy'}
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, s):
    room = Room.objects.get(id=s)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)