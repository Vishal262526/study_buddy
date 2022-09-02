from cmath import log
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from base.models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Login Page
def loginSystem(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        try:
            user = User.objects.get(username = username, password = password)
        except:
            messages.error(req,"Username Does Not Exist")

        user = authenticate(username = username, password = password)
        if user is not None:
            login(req, user)
            return redirect(req,"base/home.html")    
        else:
            messages.error(req,"Username Does Not Exist")


    return render(req,"base/login.html")

# Create your views here.
def home(req):
    myName = None


    print(myName)
    q = req.GET.get("topic") if req.GET.get("topic") != None else ""
    print(q)
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    # get all the topic details
    topics = Topic.objects.all()
    
    # get the total number of rooms
    room_count = rooms.count()

    # get the total number of topics
    topic_count = topics.count()

    print(topics)

    context = {"data":rooms,"topics":topics,"room_count":room_count,"topic_count":topic_count}
    
    return render(req,"base/home.html",context)
    

def room(req,pk):
    # get all the rooms details
    rooms = Room.objects.get(id = pk)

    # create a context to send to a template
    context = {"data":rooms}

    return render(req,"base/room.html",context)

def createRoom(req):
    form = RoomForm()
    if req.method == "POST":
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(req, 'base/room_form.html',context)

def updateRoom(req,pk):
    room = Room.objects.get(id = pk)
    if req.method == "POST":
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = RoomForm(instance=room)
        
    context = {"form":form}
    return render(req,"base/room_form.html",context)


def deleteRoom(req,pk):
    room = Room.objects.get(id = pk)
    if req.method == "POST":
        room.delete()
        return redirect("home")
    return render(req, 'base/delete.html',)    