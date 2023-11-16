from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import *


def rejalar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Reja.objects.create(
                name=request.POST.get("name"),
                date=request.POST.get("date"),
                details=request.POST.get("details"),
                status=request.POST.get("status"),
                egasi=request.user
            )
        content = {
            "rejalar": Reja.objects.filter(egasi=request.user),
            "foydalanuvchi": request.user.username.capitalize()
        }
        return render(request, "index.html", content)
    return redirect("/")


def login_view(request):
    if request.method == 'POST' and request.POST.get("forma") == "f2":
        user = authenticate(
            username=request.POST.get("l"),
            password=request.POST.get("p")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/rejalar/")
    elif request.method == 'POST' and request.POST.get("forma") == "f1":
        try:
            User.objects.create_user(
                username=request.POST.get("l"),
                password=request.POST.get("p1"),
                email=request.POST.get("email"),
            )
        finally:
            return redirect("/")
    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return redirect("/")


def reja_ochir(request, son):
    if Reja.objects.filter(egasi=request.user):
        Reja.objects.get(id=son).delete()
    return redirect("/rejalar/")


def edit(request):
    return render(request, "edit.html")


def register(request):
    return render(request, "register.html")
