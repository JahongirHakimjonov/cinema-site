from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.forms import NewsForm
from apps.hidaya.models import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    form = NewsForm
    readonly_fields = ("view_count",)
    autocomplete_fields = ("category",)
