from rest_framework import serializers

from warehouse.models import Order


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'status', 'user')
