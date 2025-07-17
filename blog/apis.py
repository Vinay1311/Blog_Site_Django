from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from master.utils import get_tokens_for_user, pagination
from helper import keys
from .permissions import IsAdmin, IsEditorOrAdmin

# User Authentication APIs

class UserRegisterAPI(generics.CreateAPIView):
    """
    API for user registration.
    
    Handl registration endpoint through patch method.
    Uses UserSerializer for validation and serialization.
    """
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        serializer = self.get_serializer(self.request.user, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response("User Registered Successfully", status=status.HTTP_200_OK)


class UserLoginAPI(generics.CreateAPIView):
    """
    API for user login.
    
    Returns JWT tokens for authenticated users.
    Uses UserLoginSerializer for validation.
    """
    serializer_class = UserLoginSerializer
    
    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.validated_data['user']
        tokens = get_tokens_for_user(user)
        return Response({keys.DATA: tokens}, status=status.HTTP_200_OK)


# Blog Management APIs

class PostBlogAPI(generics.CreateAPIView):
    """
    API for creating new blog posts.
    
    Only users with Editor or Admin role can create posts.
    Automatically sets the author to the current user.
    """
    serializer_class = PostSerializer
    permission_classes = [IsEditorOrAdmin]
    
    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EditBlogAPI(generics.UpdateAPIView):
    """
    API for editing existing blog posts.
    
    Only users with Editor or Admin role can edit posts.
    Uses partial updates to allow updating specific fields.
    """
    serializer_class = PostSerializer
    permission_classes = [IsEditorOrAdmin]
    queryset = BlogPost.objects.all()
    lookup_field = 'id'

    def patch(self, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetBlogListAPI(generics.ListAPIView):
    """
    API for listing blog posts.
    
    Supports filtering by:
    - Search term (title)
    - Category
    - Tags
    - Publication date
    
    Includes pagination support.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = BlogPost.objects.filter(status=keys.PUBLISHED)
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        date = self.request.GET.get('date')

        if search:
            queryset = queryset.filter(title__icontains=search)
        if category:
            queryset = queryset.filter(category__name=category)
        if tag:
            queryset = queryset.filter(tags__title=tag)
        if date:
            queryset = queryset.filter(published_at__date=date)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page_count = request.GET.get('page_count', 10)  # Default to 10 items per page
        page_number = request.GET.get('page_number', 1)   # Default to page 1
        
        paginated_data, pagination_info = pagination(queryset, int(page_count), int(page_number))
        serializer = self.get_serializer(paginated_data, many=True)
        
        return Response({
            'data': serializer.data,
            'pagination': pagination_info}, status=status.HTTP_200_OK)


class DeleteBlogAPI(generics.DestroyAPIView):
    """
    API for deleting blog posts.
    
    Only admin users can delete posts (handled by middleware).
    Uses custom middleware for permission checking.
    """
    # Using middleware for permission checking instead of DRF permissions
    # This allows for more granular control over delete operations
    queryset = BlogPost.objects.all()
    lookup_field = 'id'
    
    def delete(self, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({keys.ERROR: "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({keys.DATA: "Blog deleted successfully"}, status=status.HTTP_200_OK)
        
            