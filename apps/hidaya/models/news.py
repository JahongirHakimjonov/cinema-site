from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class News(AbstractBaseModel):
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    sub_title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name=_("Sub Title"),
        blank=True,
        null=True,
    )
    description = models.TextField(db_index=True, verbose_name=_("Description"))
    banner = models.ImageField(upload_to="news", verbose_name=_("Banner"))
    category = models.ForeignKey(
        "NewsCategory",
        on_delete=models.CASCADE,
        related_name="news",
        verbose_name=_("Category"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    view_count = models.BigIntegerField(default=0, verbose_name=_("View Count"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        db_table = "news"
        ordering = ["-created_at"]

    def increment_views(self):
        """Ko'rishlar sonini oshirish uchun metod."""
        self.view_count += 1
        self.save()

    def __str__(self):
        return self.title
