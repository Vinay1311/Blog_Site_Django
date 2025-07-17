from django.contrib import admin
from master.models import *
@admin.register(MasterCategory)   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(MasterTag)   
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    