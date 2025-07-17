from django.db import models
from helper.models import CreationModificationModel

class MasterCategory(CreationModificationModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class MasterTag(CreationModificationModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title