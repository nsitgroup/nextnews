from django.http import HttpResponse
from django.shortcuts import render, redirect


def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")

def cgupage(request):
    return render(request, "cgu.html")