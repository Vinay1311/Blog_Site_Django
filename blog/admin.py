from django.contrib import admin
from .models import User, BlogPost

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role']
    search_fields = ['username', 'email']
    list_filter = ['role']
    readonly_fields = ['id', 'created_at', 'updated_at']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'status', 'published_at']
    search_fields = ['title', 'author__username', 'category__name']
    list_filter = ['status', 'category']
    readonly_fields = ['id', 'created_at', 'updated_at']

