from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Info(AbstractBaseModel):
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    description = models.TextField(db_index=True, verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Info")
        verbose_name_plural = _("Infos")
        db_table = "info"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
