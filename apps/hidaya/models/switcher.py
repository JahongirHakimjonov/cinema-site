from django.db import models

from apps.shared.models import AbstractBaseModel


class Switcher(AbstractBaseModel):
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Switcher"
        verbose_name_plural = "Switchers"
        db_table = "switchers"

    def __str__(self) -> str:
        return str(self.id)
