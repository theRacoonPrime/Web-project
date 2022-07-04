from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, date


class Categories(models.Model):
    name_category = models.CharField(max_length=200)

    def __str__(self):
        return self.name_category

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default=" My awesome blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    categories = models.ManyToManyField(Categories)
    created_date = models.DateTimeField(default=timezone.now)
    postdate = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

