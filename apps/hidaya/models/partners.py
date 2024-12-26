from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Partner(AbstractBaseModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_("Name"))
    url = models.CharField(max_length=255, db_index=True, verbose_name=_("URL"))
    logo = models.ImageField(upload_to="partners", verbose_name=_("Logo"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")
        db_table = "partner"
        ordering = ["-created_at"]


class Platform(AbstractBaseModel):
    logo = models.ImageField(upload_to="platforms", verbose_name=_("Logo"))
    text = models.TextField(verbose_name=_("Text"))
    image = models.ImageField(upload_to="platforms", verbose_name=_("Image"))
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Platform")
        verbose_name_plural = _("Platforms")
        db_table = "platform"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
