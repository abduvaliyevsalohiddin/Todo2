from django.shortcuts import render


def home(requests):
    return render(requests, "index.html")


def login(requests):
    return render(requests, "login.html")


def edit(requests):
    return render(requests, "edit.html")
