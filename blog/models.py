from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from master.models import *
from helper import keys
from helper.models import CreationModificationModel

class User(AbstractUser, CreationModificationModel):
    class Role(models.Choices):
        ADMIN = keys.ADMIN
        EDITOR = keys.EDITOR
        READER = keys.READER
    
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.READER)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username


class BlogPost(CreationModificationModel):
    class BlogPostStatus(models.Choices):
        DRAFT = keys.DRAFT
        PUBLISHED = keys.PUBLISHED
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(MasterCategory, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=BlogPostStatus.choices, blank=True)
    tags = models.ManyToManyField(MasterTag, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        
    def __str__(self):
        return self.title