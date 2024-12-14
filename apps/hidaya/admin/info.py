from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.forms import InfoForm
from apps.hidaya.models import Info


@admin.register(Info)
class InfoAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    form = InfoForm
