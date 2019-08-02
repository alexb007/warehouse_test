import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    class Status:
        INPROGRESS = 'inprogress'
        PACKING = 'packaging'
        SHIPPED = 'shipped'
        CANCELED = 'canceled'

    STATUSES = (
        (Status.INPROGRESS, _('In Progress')),
        (Status.PACKING, _('Packaging')),
        (Status.SHIPPED, _('Shipped')),
        (Status.CANCELED, _('Canceled')),
    )

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        verbose_name=_('UUID')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    name = models.CharField(
        max_length=20,
        verbose_name=_('Order Name')
    )

    status = models.CharField(
        max_length=12,
        choices=STATUSES,
        default=Status.INPROGRESS,
        verbose_name=_('Order Status')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
