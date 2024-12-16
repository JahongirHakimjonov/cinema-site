from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Genre, Tags, NewsCategory, VideoCategory, BookCategory


@admin.register(Genre)
class GenreAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Tags)
class TagsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(NewsCategory)
class NewsCategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(VideoCategory)
class VideoCategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(BookCategory)
class BookCategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
