from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, Topic, Message
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name': 'Python Buddy'},
#     {'id':2, 'name': 'Java Buddy'},
#     {'id':3, 'name': 'Dart Buddy'}
# ]

def loginPage(request):
    page  = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('pass')
        flag = True
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Not Exist")
            flag = False
            
        if flag:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "User name or password doesn't Match")
            
    context = {"page":page}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error Occured During Registration..")
    page = 'register'
    context = {'page':page, "form":form}
    return render(request,'base/login_register.html',context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains = q))
    roomCount = rooms.count()
    comments = Message.objects.all()
    topic = Topic.objects.all()
    comments = Message.objects.filter(Q(room__topic__name__icontains = q))
    context = {'rooms':rooms,"topics":topic,'room_count':roomCount,'comments':comments}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    comments = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk = room.id)
    
    context = {'room': room, 'comments':comments, "participants":participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id = pk)
    rooms  = user.room_set.all()
    comments = user.message_set.all()
    topics = Topic.objects.all()
    context = {"user":user, 'rooms':rooms, 'comments':comments, "topics":topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('<h3>You are not the Creator..</h3>')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request,'base/room_form.html',context)
    
    
@login_required(login_url='/login')
def deleteRoom(request, pk):
    
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('<h3>You are not the Creator..</h3>')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj':room})


@login_required(login_url='/login')
def deleteComment(request,pk):
    comment = Message.objects.get(id=pk)
    if request.user != comment.user:
        return HttpResponse('<h3>You are not the Creator..</h3>')
    
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {"obj":comment})

        
# @login_required(login_url='/login')
# def editComment(request,pk):
#     comment = Message.objects.get(id=pk)
#     if request.user != comment.user:
#         return HttpResponse('<h3>You are not the Creator..</h3>')
    
#     if request.method == 'POST':
#         comment.body = request.POST.get('edittedComment')
#         comment.save(update_fields=('body',))
#         return redirect('home')
    
#     return render(request, 'base/edit.html', {"obj":comment})
        