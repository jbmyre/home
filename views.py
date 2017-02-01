from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from .models import Page, Post, Photo


def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register.html')


def birthdays(request):
    return render(request, 'home/birthdays.html')


def ycs(request):
    post = Post.objects.filter(page__name='YCS').all()
    pic = Photo.objects.filter(page__name='YCS').all()
    posts = dict(posts=post, pics=pic)
    return render(request, 'home/ycs.html', posts)


def ps6(request):
    return render(request, 'home/ps6.html')


def spring(request):
    return render(request, 'home/spring.html')