from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Notification


@admin.register(Notification)
class NotificationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ["id", "title", "message", "created_at"]
    search_fields = ["title", "message"]
    list_per_page = 50
