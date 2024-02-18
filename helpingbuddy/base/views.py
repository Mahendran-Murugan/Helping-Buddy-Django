from django.shortcuts import render

rooms = [
    {'id':1, 'name': 'Python Buddy'},
    {'id':2, 'name': 'Java Buddy'},
    {'id':3, 'name': 'Dart Buddy'}
]

def home(request):
    return render(request, 'home.html', {'rooms':rooms});

def room(request):
    return render(request, 'room.html');
