from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Comments(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    postdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Likes(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

















