from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete


class WarehouseConfig(AppConfig):
    name = 'warehouse'

    def ready(self):
        from .models import Order
        from .signals import order_saved_handler, order_deleted_handler
        post_save.connect(order_saved_handler, sender=Order)
        post_delete.connect(order_deleted_handler, sender=Order)
