from django.conf import settings
from rest_framework import permissions
from rest_framework.authentication import get_authorization_header


class ApiKeyPermission(permissions.BasePermission):
    """
    Allow action only for application with valid api_key
    """

    def has_permission(self, request, view):
        return settings.API_KEY == get_authorization_header(request).decode() or request.user.is_superuser
