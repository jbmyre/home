# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-25 15:24
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='home.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/slider')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='home.Photo'),
        ),
    ]
