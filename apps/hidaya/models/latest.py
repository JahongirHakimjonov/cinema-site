# from PIL import Image
# from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class LatestNews(AbstractBaseModel):
    link = models.CharField(
        max_length=255, db_index=True, verbose_name=_("Link"), blank=True, null=True
    )
    banner = models.ImageField(upload_to="latest_news", verbose_name=_("Image 16:9"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    # def clean(self):
    #     if self.banner:
    #         image = Image.open(self.banner)
    #         width, height = image.size
    #         if width / height != 16 / 9:
    #             raise ValidationError(_("Image must have a 16:9 aspect ratio"))

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name = _("Latest News")
        verbose_name_plural = _("Latest News")
        ordering = ("-created_at",)
        db_table = "latest_news"
