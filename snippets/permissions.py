from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Custom permission to only allow owners of an object to edit or delete it. """

    def has_object_permission(self, request, view, obj):
        # safe permissions are always allowed (such as GET - read, HEAD and OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to owner of snippets
        return obj.owner == request.user