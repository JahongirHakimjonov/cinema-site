from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.models import LatestNews


@admin.register(LatestNews)
class LatestNewsAdmin(ModelAdmin):
    list_display = ("id", "link", "is_active")
    list_filter = ("is_active",)
    search_fields = ("link",)
    readonly_fields = ("created_at", "updated_at")
