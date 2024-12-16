from modeltranslation.translator import TranslationOptions, register

from apps.hidaya.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title", "description")
