from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from .models import Page, Post, Photo, Slider, SliderImage


def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register.html')


def birthdays(request):
    post = Post.objects.filter(page__name='birthdays').all()
    pic = Photo.objects.filter(page__name='birthday').all()
    slider = SliderImage.objects.select_related().filter(page__name='birthday').all()
    posts = dict(posts=post, pics=pic, slider=slider)
    return render(request, 'home/birthdays.html', posts)


def ycs(request):
    post = Post.objects.filter(page__name='YCS').all()
    pic = Photo.objects.filter(page__name='YCS').all()
    slider = SliderImage.objects.select_related().filter(page__name="YCS").all()
    posts = dict(posts=post, pics=pic, slider=slider)
    return render(request, 'home/ycs.html', posts)


def ps6(request):
    post = Post.objects.filter(page__name='ps6').all()
    pic = Photo.objects.filter(page__name='ps6').all()
    slider = SliderImage.objects.select_related().filter(page__name='ps6').all()
    posts = dict(posts=post, pics=pic, slider=slider)
    return render(request, 'home/ps6.html', posts)


def spring(request):
    post = Post.objects.filter(page__name='spring').all()
    pic = Photo.objects.filter(page__name='spring').all()
    slider = SliderImage.objects.select_related().filter(page__name='spring').all()
    posts = dict(posts=post, pics=pic, slider=slider)
    return render(request, 'home/spring.html', posts)
