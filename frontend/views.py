from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from user_profile.forms import UserForm
from user_profile.models import MainCycle
import services
import re


def index(request):
    relocate, template, params = services.clicker_services.main_page(request)
    if relocate:
        return redirect(template)
    return render(request, template, params)


def user_login(request):
    relocate, template, params = services.auth_services.user_login(request)
    if relocate:
        return redirect(template)
    return render(request, template, params)


def user_logout(request):
    template = services.auth_services.user_logout(request)
    return redirect(template)


def user_registration(request):
    relocate, template, params = services.auth_services.user_registration(request)
    if relocate:
        return redirect(template)
    return render(request, template, params)

