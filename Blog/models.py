from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
  blog_title=models.CharField(max_length=250)
  blog_image=models.ImageField(upload_to='blogImage/')
  blog_summary=models.CharField(max_length=200,blank=True)
  blog_description= models.TextField()


# Create your models here.
