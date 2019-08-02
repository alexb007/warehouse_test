from rest_framework import viewsets, status
from rest_framework.response import Response

from core.permissions import ApiKeyPermission
from warehouse.models import Order
from warehouse.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [ApiKeyPermission]

    def get_queryset(self):
        return Order.objects.all().order_by('created_at', 'updated_at')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)
