from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .models import Room,Topic,Message,User
from .forms import RoomForm,UserForm,MyUserCreationForm


def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST.get('email').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            messages.error(request,'User does not exits')
        
        user=authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Email or Password does not exists')



    context={'page':page}
    return render(request,'base/login_register.html',context)


def logoutPage(request):
    logout(request)
    return redirect('home')

def UserRegister(request):
    form=MyUserCreationForm()

    if request.method == 'POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'There is an error while Registration')
    return render(request,'base/login_register.html',{'form':form})

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
     
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
        )
    topic=Topic.objects.all()[0:4]
    room_count=rooms.count()
    room_message=Message.objects.filter(Q(room__topic__name__icontains=q))

    context={'room':rooms,'topic':topic,'room_count':room_count,'room_message':room_message}
    return render(request,'base/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    participants=room.participants.all()

    if request.method == 'POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    
    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)

def UserProfile(request,pk):
    user=User.objects.get(id=pk)
    room=user.room_set.all()
    room_message=user.message_set.all()
    topic=Topic.objects.all()
    context={'user':user,'room':room,'room_message':room_message,'topic':topic}
    return render(request,'base/profile.html',context)

@login_required(login_url='login')
def create_room(request):
    form=RoomForm()
    topics=Topic.objects.all()
    if request.method=='POST':

        topic_name=request.POST.get('topic')
        topic, created= Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect("home")


    context={'form':form,'topics':topics}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def update_room(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    topics=Topic.objects.all()
    if request.user!=room.host:
        return HttpResponse("You are not allowed here")

    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic, created= Topic.objects.get_or_create(name=topic_name)
        room.name=request.POST.get('name')
        room.topic=topic
        room.description=request.POST.get('description')
        room.save()
        return redirect("home")
        
    context={'form':form,'topics':topics,'room':room}
    return render(request,'base/room_form.html',context)


@login_required(login_url='login')
def delete_room(request,pk):
    room=Room.objects.get(id=pk)

    if request.user!=room.host:
        return HttpResponse("You are not allowed here")

    if request.method=='POST':
        room.delete()
        return redirect("home")
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url='login')
def delete_message(request,pk):
    message=Message.objects.get(id=pk)

    if request.user!=message.user:
        return HttpResponse("You are not allowed here")

    if request.method=='POST':
        message.delete()
        return redirect("home")
    return render(request,'base/delete.html',{'obj':message})

@login_required(login_url='login')
def update_user(request):
    user=request.user
    form=UserForm(instance=user)

    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile',pk=user.id)
    return render(request,'base/update_user.html',{'form':form})


def topics_page(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    topics=Topic.objects.filter(name__icontains=q)
    return render(request,'base/topics.html',{'topics':topics})

def activity_page(request):
    room_message=Message.objects.all()
    return render(request,'base/activity.html',{'room_message':room_message})