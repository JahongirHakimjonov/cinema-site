from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Genre, BookCategory, NewsCategory, VideoCategory, Tags


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(BookCategory)
class BookCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(VideoCategory)
class VideoCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ("name",)
