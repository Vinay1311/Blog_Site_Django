from rest_framework import serializers
from .models import BlogPost, User, MasterCategory, MasterTag
from master.serializers import CategorySerializer, TagSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role']
        read_only_fields = ['role']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'status', 'published_at']
    
    def create(self, validated_data):
        category_data = validated_data.pop('category', None)
        category = None
        if category_data:
            category, _ = MasterCategory.objects.get_or_create(**category_data)

        tag_data = validated_data.pop('tags', None)
        tags = []
        if tag_data:
            for tag in tag_data:
                tag, _ = MasterTag.objects.get_or_create(**tag)
                tags.append(tag)
        
        post = BlogPost.objects.create(
            author=self.context['request'].user,
            category=category,
            tags=tags,
            **validated_data
        )
        return post
