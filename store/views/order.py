from rest_framework import viewsets

from store.models import Order
from store.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().select_related('user').order_by('created_at', 'updated_at')
