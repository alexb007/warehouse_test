import json

from warehouse.serializers import OrderSerializer
from warehouse.tasks import update_order, delete_order


def order_saved_handler(sender, instance, created, **kwargs):
    if not created:
        order = OrderSerializer(instance).data
        update_order.apply_async(args=(order,))


def order_deleted_handler(sender, instance, **kwargs):
    delete_order.apply_async(args=(instance.id,))
