from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/')


class Page(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name="photo"
    )

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="post"
    )
    content = RichTextUploadingField(null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title


