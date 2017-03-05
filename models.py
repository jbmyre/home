from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = RichTextUploadingField(null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title


class Page(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    posts = models.ManyToManyField(Post)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class SliderImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='static/home/uploads/', blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title


class Slider(models.Model):
    page = models.ForeignKey(Page)
    image = models.ForeignKey(SliderImage)

    def __str__(self):  # __unicode__ on Python 2
        return self.page.name


class Photo(models.Model):
    title = models.CharField(max_length=100)
    page = models.ForeignKey(Page)
    image = models.ImageField(upload_to='static/home/uploads/', blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title


