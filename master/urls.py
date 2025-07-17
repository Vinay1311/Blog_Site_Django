from django.urls import path
from .apis import *

urlpatterns = [
    path('add-category/', AddCategoryAPI.as_view(), name='add_category'),
    path('add-tag/', AddTagAPI.as_view(), name='add_tag'),
]