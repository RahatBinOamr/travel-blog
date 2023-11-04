from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class Blog(models.Model):
  blog_title=models.CharField(max_length=250)
  blog_image=models.ImageField(upload_to='blogImage/')
  blog_summary=models.CharField(max_length=200,blank=True)
  blog_description= models.TextField()
  blog_slug = AutoSlugField(populate_from='blog_title',blank=True)


# Create your models here.
