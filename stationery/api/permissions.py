from rest_framework.permissions import SAFE_METHODS, BasePermission


class CanCreateEditDeleteComments(BasePermission):
    """Authenticated user has permission to work with comments"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Check if user is author of publication"""
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
