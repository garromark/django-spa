from rest_framework import permissions

class IsSelf(permissions.BasePermission):
    """
    Used to enforce the fact that users can only
    see their own profile.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsStaff(permissions.BasePermission):
    """
    True if the user object is a memeber of the staff
    i.e. has the is_staff flag set to true
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
