from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class NotificationType(models.TextChoices):
    SINGLE = "SINGLE", _("Single")
    ALL = "ALL", _("All")


class Notification(AbstractBaseModel):
    banner = models.FileField(
        upload_to="notifications",
        null=True,
        blank=True,
        verbose_name=_("Banner"),
    )
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    message = models.TextField(db_index=True, verbose_name=_("Message"))

    class Meta:
        db_table = "notifications"
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ["-created_at"]

    def __str__(self):
        return self.message
