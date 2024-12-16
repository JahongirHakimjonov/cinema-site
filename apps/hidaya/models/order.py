from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.hidaya.choices import PaymentMethodChoices
from apps.hidaya.models import Book
from apps.shared.models import AbstractBaseModel


class FormatChoices(models.TextChoices):
    PDF = "ELECTRONIC", _("Electronic")
    PHYSICAL = "PHYSICAL", _("Physical")


class Order(AbstractBaseModel):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="purchases", verbose_name=_("Book")
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name=_("User")
    )
    format = models.CharField(
        max_length=10, choices=FormatChoices, verbose_name=_("Format")
    )
    address = models.JSONField(blank=True, null=True, verbose_name=_("Address"))
    payment_status = models.BooleanField(
        default=False, verbose_name=_("Payment Status")
    )
    total_price = models.DecimalField(
        max_digits=100, decimal_places=2, verbose_name=_("Total Price")
    )
    payment_method = models.CharField(
        max_length=100,
        choices=PaymentMethodChoices,
        default=PaymentMethodChoices.PAYME,
    )

    def save(self, *args, **kwargs):
        if self.format == "physical" and not self.address:
            raise ValueError(_("Address is required for physical book purchases"))
        self.total_price = self.book.get_discount_price()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = "order"
        ordering = ["-created_at"]
        # unique_together = ["book", "user", "format"]

    def __str__(self) -> str:
        return f"{self.book.title} - {self.user.username} - {self.format}"
