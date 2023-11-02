from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  list_display=('blog_title', 'blog_image', 'blog_summary', 'blog_description')
admin.site.register(Blog, BlogAdmin)
