from django.shortcuts import render

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
