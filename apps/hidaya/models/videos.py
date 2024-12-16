from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Video(AbstractBaseModel):
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    description = models.TextField(db_index=True, verbose_name=_("Description"))
    banner = models.ImageField(upload_to="videos/banner", verbose_name=_("Banner"))
    tags = models.ManyToManyField("Tags", related_name="videos", verbose_name=_("Tags"))
    category = models.ForeignKey(
        "VideoCategory",
        on_delete=models.CASCADE,
        related_name="videos",
        verbose_name=_("Category"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    date = models.DateField(verbose_name=_("Date"))
    original_file = models.FileField(
        upload_to="videos/original", verbose_name=_("Original File")
    )
    view_count = models.BigIntegerField(
        default=0, verbose_name=_("View Count"), editable=False
    )
    hls_playlist = models.FileField(
        upload_to="videos/hls_playlist",
        verbose_name=_("HLS Playlist"),
        null=True,
        blank=True,
    )

    def increment_views(self):
        """Ko'rishlar sonini oshirish uchun metod."""
        self.view_count += 1
        self.save()

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        db_table = "video"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
