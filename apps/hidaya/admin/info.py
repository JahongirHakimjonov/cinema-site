from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.forms import InfoForm
from apps.hidaya.models import Info


@admin.register(Info)
class InfoAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    form = InfoForm
