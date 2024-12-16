from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "author", "price", "created_at")
    search_fields = ("title", "author")
    autocomplete_fields = ("genre", "category")
    readonly_fields = ("created_at", "updated_at", "sold_count")
