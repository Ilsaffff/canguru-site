from rest_framework import permissions


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):
    edit_methods = ['PUT', 'PATCH']

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.email == request.user.email:
            return True
        if request.user.is_staff and request.method not in self.edit_methods:
            return True
        if request.user.is_superuser:
            return True
        return False
