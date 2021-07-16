from rest_framework.permissions import BasePermission


class BoardPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST' or request.method == 'PATCH' or request.method == 'DELETE':
            if not request.user.is_staff and request.user.is_authenticated:
                return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        elif request.method == 'POST' or request.method == 'PATCH' or request.method == 'DELETE':
            if obj.author == request.user:
                return True

        return False
