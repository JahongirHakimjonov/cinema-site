from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.forms import NewsForm
from apps.hidaya.models import News


@admin.register(News)
class NewsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    form = NewsForm
    readonly_fields = ("view_count",)
    autocomplete_fields = ("category",)
