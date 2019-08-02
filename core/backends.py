from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class DisabledHTMLFilterBackend(DjangoFilterBackend):

    def to_html(self, request, queryset, view):
        return ""
