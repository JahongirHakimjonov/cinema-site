from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Partner


@admin.register(Partner)
class PartnerAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "url", "is_active", "created_at")
    search_fields = ("name", "url")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("is_active",)
