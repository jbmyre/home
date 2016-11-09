from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Page(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=128)
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="post"
    )
    text = models.TextField()
