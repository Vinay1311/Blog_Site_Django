"""
Middleware to restrict blog deletion to admin users only.

This middleware ensures that only users with admin role can delete blog posts.
It intercepts DELETE requests to the blog delete endpoint and verifies user permissions.
"""

from django.http import JsonResponse
from rest_framework import status
from helper import keys

class RestrictDeleteBlogToAdminMiddleware:
    """
    Middleware class to restrict blog deletion to admin users.
    
    This middleware:
    1. Intercepts DELETE requests to blog delete endpoints
    2. Verifies user authentication
    3. Checks user role against admin role
    4. Returns appropriate error messages for unauthorized access
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Only process DELETE requests to delete blog endpoint
        if request.method == 'DELETE' and '/delete_blog/' in request.path:
            # Verify user is authenticated
            if not request.user.is_authenticated:
                return JsonResponse(
                    {'error': 'Authentication required'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
            # Verify user has admin role
            if request.user.role != keys.ADMIN:
                return JsonResponse(
                    {'error': 'Only admin users can delete posts'},
                    status=status.HTTP_403_FORBIDDEN
                )
        
        return self.get_response(request)