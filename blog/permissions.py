# blog/permissions.py
from rest_framework.permissions import BasePermission
from helper import keys

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == keys.ADMIN

class IsEditorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [keys.ADMIN, keys.EDITOR]

    def has_object_permission(self, request, view, obj):
        return request.user.role == keys.ADMIN or obj.author == request.user

class IsReaderOrPublished(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [keys.READER, keys.EDITOR, keys.ADMIN]

    def has_object_permission(self, request, view, obj):
        if request.user.role in [keys.READER, keys.EDITOR, keys.ADMIN]:
            return obj.status == keys.PUBLISHED
        return True


