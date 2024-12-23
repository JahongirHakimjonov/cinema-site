import io

from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.shared.models import AbstractBaseModel
from apps.users.managers import UserManager


class RoleChoices(models.TextChoices):
    ADMIN = "ADMIN", _("Admin")
    USER = "USER", _("Foydalanuvchi")
    MODERATOR = "MODERATOR", _("Moderator")


class User(AbstractUser, AbstractBaseModel):
    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Telefon raqami"),
        db_index=True,
    )
    username = models.CharField(
        max_length=100,
        verbose_name=_("Foydalanuvchi nomi"),
        db_index=True,
    )
    avatar = models.ImageField(
        upload_to="avatars/", null=True, blank=True, verbose_name=_("Avatar")
    )
    role = models.CharField(
        choices=RoleChoices.choices,
        max_length=20,
        default=RoleChoices.USER,
        verbose_name=_("Role"),
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.phone}"
            if self.phone
            else str(_("Foydalanuvchi"))
        )

    def save(self, *args, **kwargs):
        self.username = self.phone
        if self.avatar:
            img = Image.open(self.avatar)
            if img.format != "WEBP":
                img_io = io.BytesIO()
                img.save(img_io, format="WEBP", quality=100)
                self.avatar.save(
                    f"{self.avatar.name.split('.')[0]}.webp",
                    ContentFile(img_io.getvalue()),
                    save=False,
                )
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Foydalanuvchilar")
        ordering = ["-created_at"]
        db_table = "users"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class ActiveSessions(AbstractBaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sessions", verbose_name=_("User")
    )
    ip = models.GenericIPAddressField(db_index=True, verbose_name=_("IP address"))
    user_agent = models.TextField(verbose_name=_("User agent"), db_index=True)
    location = models.JSONField(verbose_name=_("Location"), null=True, blank=True)
    last_activity = models.DateTimeField(
        auto_now=True, verbose_name=_("Last activity"), db_index=True
    )
    fcm_token = models.CharField(
        max_length=255,
        verbose_name=_("FCM token"),
        null=True,
        blank=True,
        db_index=True,
    )
    refresh_token = models.TextField(verbose_name=_("Refresh token"), db_index=True)
    access_token = models.TextField(verbose_name=_("Access token"), db_index=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    data = models.JSONField(verbose_name=_("Data"), null=True, blank=True)

    class Meta:
        verbose_name = _("Active session")
        verbose_name_plural = _("Active sessions")
        db_table = "active_sessions"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} {self.ip}" if self.user else str(_("Session"))
