from django.shortcuts import render, redirect
from django.http import Http404

from django.db import IntegrityError
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			room_code = request.POST.get("room_code")
			char_choice = request.POST.get("character_choice")
			return redirect(
            '/play/%s?&choice=%s' 
            %(room_code, char_choice)
        )

		return render(request,"game/index.html")
	else:
		return render(request,"game/login.html")



def register(request):
	if request.method =="POST":
		username = request.POST["name"]
		email = request.POST['email']
		password = request.POST['password']
		conform = request.POST['conform']
		if password !=conform:
			return render(request,"game/register.html",{"message":"Password not match"})

		try:
			user = User.objects.create_user(username,email,password)
			user.save()
		except IntegrityError:

			return render(request,"game/register.html",{"message":"Username already taken"})

		login(request,user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "game/register.html")
		

def login_view(request):
	if request.method =="POST":
		username = request.POST['user']
		password = request.POST['password']

		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request,"game/login.html",{"message":"Invalid username and/or password."})
	else:
		return render(request,"game/login.html")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))


def game(request, room_code):
    choice = request.GET.get("choice")
    if choice not in ['X', 'O']:
        raise Http404("Choice does not exists")
    context = {
        "char_choice": choice, 
        "room_code": room_code
    }
    return render(request, "game/game.html", context)