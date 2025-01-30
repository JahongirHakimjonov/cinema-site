from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.models.switcher import Switcher


@admin.register(Switcher)
class SwitcherAdmin(ModelAdmin):
    list_display = ("id", "is_active")
    list_display_links = ("id",)
