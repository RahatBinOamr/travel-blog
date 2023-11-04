from django.contrib import admin
from .models import Blog, Comment, Contact

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_slug', 'blog_image',
                    'blog_summary', 'blog_description')


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'comment')


admin.site.register(Comment, CommentAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(Contact, ContactAdmin)
