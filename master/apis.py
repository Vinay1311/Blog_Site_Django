from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class AddCategoryAPI(generics.CreateAPIView):
    """Add Category API"""
    serializer_class = CategorySerializer   
    permission_classes = [IsAuthenticated]
    
    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddTagAPI(generics.CreateAPIView):
    """Add Tag API"""
    serializer_class = TagSerializer   
    permission_classes = [IsAuthenticated]
    
    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        