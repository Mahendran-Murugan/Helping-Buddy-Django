from django.shortcuts import render

rooms = [
    {'id':1, 'name': 'Python Buddy'},
    {'id':2, 'name': 'Java Buddy'},
    {'id':3, 'name': 'Dart Buddy'}
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, s):
    room = None
    for i in rooms:
        if i['id'] == int(s):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
