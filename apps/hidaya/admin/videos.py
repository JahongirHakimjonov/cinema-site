from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Video


@admin.register(Video)
class VideoAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    autocomplete_fields = ("tags", "category")
