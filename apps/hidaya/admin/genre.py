from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.hidaya.models import Genre, Tags, NewsCategory, VideoCategory, BookCategory


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Tags)
class TagsAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(NewsCategory)
class NewsCategoryAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(VideoCategory)
class VideoCategoryAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(BookCategory)
class BookCategoryAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
