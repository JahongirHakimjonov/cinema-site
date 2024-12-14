from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Genre(AbstractBaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Name")
    )

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")
        db_table = "genre"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BookCategory(AbstractBaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Name")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Book Category")
        verbose_name_plural = _("Book Categories")
        db_table = "books_category"
        ordering = ["name"]

    def __str__(self):
        return self.name


class NewsCategory(AbstractBaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Name")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("News Category")
        verbose_name_plural = _("News Categories")
        db_table = "news_category"
        ordering = ["name"]

    def __str__(self):
        return self.name


class VideoCategory(AbstractBaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Name")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Video Category")
        verbose_name_plural = _("Video Categories")
        db_table = "video_category"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tags(AbstractBaseModel):
    name = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Name")
    )

    class Meta:
        verbose_name = _("Tags")
        verbose_name_plural = _("Tags")
        db_table = "tags"
        ordering = ["name"]

    def __str__(self):
        return self.name
