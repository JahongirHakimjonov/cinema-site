from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import Book


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title", "description", "author")
