from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Book(AbstractBaseModel):
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    sub_title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name=_("Sub Title"),
        blank=True,
        null=True,
    )
    description = models.TextField(db_index=True, verbose_name=_("Description"))
    author = models.CharField(max_length=255, db_index=True, verbose_name=_("Author"))
    banner = models.ImageField(upload_to="books", verbose_name=_("Banner"))
    pages = models.BigIntegerField(verbose_name=_("Pages"))
    date = models.DateField(verbose_name=_("Date"))
    price = models.DecimalField(
        max_digits=100, decimal_places=2, verbose_name=_("Price")
    )
    discount_price = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        verbose_name=_("Discount Price"),
        blank=True,
        null=True,
        default=0,
    )
    category = models.ForeignKey(
        "BookCategory",
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name=_("Category"),
    )
    genre = models.ManyToManyField(
        "Genre", related_name="books", verbose_name=_("Genre")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    file = models.FileField(upload_to="books", verbose_name=_("File"))
    original_file = models.FileField(
        upload_to="books/original",
        verbose_name=_("Original File"),
        blank=True,
        null=True,
    )
    sold_count = models.BigIntegerField(default=0, verbose_name=_("Sold Count"))

    def get_discount_price(self):
        if self.discount_price > 0 and self.discount_price is not None:
            return self.discount_price
        return self.price

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        db_table = "book"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
