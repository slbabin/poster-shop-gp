from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Updating order total on orderitem update or create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Updating order total on orderitem delete
    """
    instance.order.update_total()
    