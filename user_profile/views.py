from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializator import UserSerializer, UserSerializeDetails
from rest_framework import generics
import re


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializeDetails


def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        return render(request, 'index.html', {'user': user[0]})
    else:
        return redirect('login')


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'user': user})
        else:
            return render(request, 'login.html', {'invalid': True})
    else:
        return render(request, 'login.html', {'invalid': False})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        existing_user = User.objects.filter(username=username)
        if len(existing_user) == 0:
            password = request.POST["password"]
            if not check_password_safety(password):
                return render(request, 'registration.html', {'invalid': True})
            user = User.objects.create_user(username, '', password)
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return render(request, 'index.html', {'user': user})
        else:
            return render(request, 'registration.html', {'invalid': True})
    else:
        return render(request, 'registration.html', {'invalid': False})


def check_password_safety(password):
    pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{6,}$')
    return pattern_password.match(password)
