from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import *


def rejalar(requests):
    if requests.user.is_authenticated:
        if requests.method == 'POST':
            Reja.objects.create(
                name=requests.POST.get("name"),
                date=requests.POST.get("date"),
                details=requests.POST.get("details"),
                status=requests.POST.get("status"),
                egasi=requests.user
            )
        content = {
            "rejalar": Reja.objects.filter(egasi=requests.user),
            "foydalanuvchi": requests.user.username.capitalize()
        }
        return render(requests, "index.html", content)
    return redirect("/")


def login_view(requests):
    if requests.method == 'POST':
        user = authenticate(
            username=requests.POST.get("l"),
            password=requests.POST.get("p")
        )
        if user is None:
            return redirect("/")
        login(requests, user)
        return redirect("/rejalar/")
    return render(requests, "login.html")


def logout_view(requests):
    logout(requests)
    return redirect("/")


def edit(requests):
    return render(requests, "edit.html")
