from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethodChoices(models.TextChoices):
    CLICK = "CLICK", _("Click")
    PAYME = "PAYME", _("Payme")
    OCTO = "OCTO", _("OCTO")
    CASH = "CASH", _("Cash")
