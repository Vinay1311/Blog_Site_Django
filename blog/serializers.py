from rest_framework import serializers
from .models import BlogPost, User, MasterCategory, MasterTag
from master.serializers import CategorySerializer, TagSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role']
        # read_only_fields = ['role']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=MasterCategory.objects.all(), required=False, allow_null=True
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=MasterTag.objects.all(), many=True, required=False
    )

    class Meta:
        model = BlogPost
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        category = validated_data.pop('category', None)

        blog = BlogPost.objects.create(category=category, **validated_data)
        blog.tags.set(tags_data)
        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        category = validated_data.pop('category', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if category is not None:
            instance.category = category
        instance.save()

        if tags_data is not None:
            instance.tags.set(tags_data)
        return instance
