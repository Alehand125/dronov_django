from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp", "email")


admin.site.register(BlogPost, BlogPostAdmin)
