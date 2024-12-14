from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ("title", "author", "price", "created_at")
    search_fields = ("title", "author")
    autocomplete_fields = ("genre", "category")
    readonly_fields = ("created_at", "updated_at", "sold_count")
