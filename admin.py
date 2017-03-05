from django.contrib import admin

# Register your models here.
from .models import Page, Post, Photo, Slider, SliderImage

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Slider)
#admin.site.register(SliderImage)