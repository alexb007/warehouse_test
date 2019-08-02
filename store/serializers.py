from rest_framework import serializers

from store.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'status', 'user')
