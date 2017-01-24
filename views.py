from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register.html')


def birthdays(request):
    return render(request, 'home/birthdays.html')


def ycs(request):
    return render(request, 'home/ycs.html')


def ps6(request):
    return render(request, 'home/ps6.html')


def spring(request):
    return render(request, 'home/spring.html')