from rest_framework import permissions
from rest_framework.fields import get_attribute


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            get_attribute(obj, getattr(obj, "user_attribute", "user").split("."))
            == request.user
        )


class IsOwnerOrReadOnly(IsOwner):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or super().has_object_permission(request, view, obj)
        )
