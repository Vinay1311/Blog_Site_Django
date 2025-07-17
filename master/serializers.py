from rest_framework import serializers
from .models import MasterCategory, MasterTag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCategory
        fields = ['id', 'name', 'description']  


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTag
        fields = ['id', 'title', 'description']