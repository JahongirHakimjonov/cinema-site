from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Video


@admin.register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    autocomplete_fields = ("tags", "category")
