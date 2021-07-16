from rest_framework.permissions import BasePermission


class CardPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST' or request.method == 'DELETE':
            if not request.user.is_authenticated and not request.user.is_staff:
                return False

        return True

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True

        return False