from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.hidaya.models import Order


@receiver(post_save, sender=Order)
def check_order_status(sender, instance, **kwargs):
    if instance.payment_status:
        instance.book.sold_count += 1
        instance.book.save()
