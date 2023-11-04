from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_image = models.ImageField(upload_to='blogImage/')
    blog_summary = models.CharField(max_length=200, blank=True)
    blog_description = HTMLField()
    blog_slug = AutoSlugField(populate_from='blog_title', blank=True)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(blank=True)
